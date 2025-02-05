#!/usr/bin/env node
// make_heliostat.js

import { exec } from "child_process";
import { promisify } from 'util';

const c_Parts = {
	heliostat: 'heliostat_v01',
	heliostat_2: 'heliostat_2_v01',
	base: 'base_v01',
	pole_static: 'pole_static_v01',
	vaxis: 'vaxis_v01',
	vaxis_holder_A: 'vaxis_holder_A_v01',
	vaxis_holder_B1: 'vaxis_holder_B1_v01',
	vaxis_holder_B2: 'vaxis_holder_B2_v01',
	ring: 'ring_v01',
	ring_guidance: 'ring_guidance_v01',
	vaxis_guidance: 'vaxis_guidance_v01',
	rake: 'rake_v01',
	rake_stopper: 'rake_stopper_v01',
	haxis_guidance: 'haxis_guidance_v01',
	spider: 'spider_v01',
	swing: 'swing_v01',
	rod: 'rod_v01',
	trapeze: 'trapeze_v01',
	surface: 'surface_v01'
};

const c_svgdxf = {
	heliostat: ['faceSide', 'faceFace'],
	heliostat_2: ['faceSide', 'faceFace', 'faceTop'],
	base: ['faceCut', 'faceTop', 'faceHollow'],
	pole_static: ['poleCut', 'poleFace', 'poleBottom', 'emptyPole', 'emptyDoor', 'holderB2Section', 'holderB2Top', 'holderB1Section', 'holderB1Top', 'holderASection', 'holderATop'],
	vaxis: ['faceCut', 'faceBottom'],
	vaxis_holder: ['facePetal', 'faceOuter', 'faceButtress1', 'faceButtress2', 'faceButtress12'],
	ring: ['faceRingBase', 'faceRingTeeth', 'faceSection'],
	ring_guidance: ['faceTop', 'faceSection'],
	vaxis_guidance: ['faceTop', 'faceSection'],
	rake: ['faceCone', 'faceConeHollow', 'faceBeam', 'faceBeamHollow', 'faceDisc', 'faceHand', 'faceWing', 'faceWingHollow', 'faceDoor'],
	rake_stopper: [], // too much figures (18), so skipped
	haxis_guidance: ['faceProfile', 'faceSide'],
	spider: ['faceLegs', 'faceTube', 'faceBody'],
	swing: ['faceSide', 'faceFace', 'faceTop', 'faceButtress', 'faceTopWithRods'],
	rod: ['faceCut', 'facePlate', 'faceTop'],
	trapeze: ['faceFrame', 'facePlate', 'faceRod', 'faceRodHollow', 'faceCutRod'],
	surface: ['faceSurface', 'faceOnePanel']
};

function inferDesignName(instanceName) {
	const re = /_[A-Z][0-9]*$/;
	const rDesignName = instanceName.replace(re, '');
	return rDesignName
}

function getCmd(dName, fName) {
	const desiName = inferDesignName(dName);
	console.log(`info456: reference name: ${dName}   design name: ${desiName}`);
	const rCmd = [];
	//rCmd.push('pwd');
	//rCmd.push(`ls refs/${dName}`);
	//rCmd.push(`npx designix-cli -d=heliostat/${desiName} -o=refs/${dName} --outFileName=px_${fName}.json write json_param`);
	rCmd.push(`npx designix-cli -d=heliostat/${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}.log.txt write compute_log`);
	// svg, dxf
	for (const face of c_svgdxf[desiName]) {
		rCmd.push(`npx designix-cli -d=heliostat/${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}_${face}.svg write svg__${face}`);
		rCmd.push(`npx designix-cli -d=heliostat/${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}_${face}.dxf write dxf__${face}`);
	}
	// paxJson
	rCmd.push(`npx designix-cli -d=heliostat/${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}.pax.json write pax_all`);
	// OpenSCAD
	rCmd.push(`npx designix-cli -d=heliostat/${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}.scad write scad_3d_openscad`);
	//rCmd.push(`openscad -o refs/${dName}/${fName}_oscad.stl refs/${dName}/${fName}.scad`);
	// JsCAD
	rCmd.push(`npx designix-cli -d=heliostat/${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}.js write js_3d_openjscad`);
	//rCmd.push(`cd refs && npx jscad ${dName}/${fName}.js -o ${dName}/${fName}_jscad.stl`);
	// FreeCAD
	rCmd.push(`npx designix-cli -d=heliostat/${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}.py write py_3d_freecad`);
	//rCmd.push(`freecad.cmd refs/${dName}/${fName}.py refs/${dName}/${fName}_fc`);
	//rCmd.push(`npx rimraf refs/${dName}`);
	return rCmd
}

const aExec = promisify(exec);

async function execCmd(cmd) {
	console.log(cmd);
	try {
		const { stdout, stderr } = await aExec(cmd);
		console.log('---> stdout:');
		console.log(stdout);
		console.log('---> stderr:');
		console.log(stderr);
		console.log('---> end of log');
	} catch (err) {
		console.log(`err895: Error by executing: ${cmd}`);
		console.log(err);
		console.log(`info895: script stopped!`);
		process.exit(1);
	}
}

async function loopDesign(dList) {
	const pList = Object.keys(c_Parts);
	for (const [ idx, oneDesign ] of dList.entries()) {
		const idx2 = idx + 1;
		console.log(`${idx2} : working on ${oneDesign}`);
		if (!pList.includes(oneDesign)) {
			console.log(`err309: design ${oneDesign} is unkown!`);
			process.exit(1);
		}
		const cmds = getCmd(oneDesign, c_Parts[oneDesign]);
		for (const oneCmd of cmds) {
			await execCmd(oneCmd);
		}
		console.log(`${idx2} : end of generation of ${oneDesign}`);
	}
}

async function mhcli(args) {
	//console.log(args);
	const c_flag_all = '--all';
	const allList = Object.keys(c_Parts);
	if (args.length === 3 && args[2] === c_flag_all) {
		await loopDesign(allList);
	} else if (args.length > 2) {
		await loopDesign(args.slice(2));
	} else {
		console.log('err206: no argument provided!');
		console.log(`Possible arguments: ${c_flag_all} or the following design names:`);
		let str1 = '';
		let str2 = '';
		for (const [ idx, oneDesign ] of allList.entries()) {
			str1 += ` ${oneDesign}`;
			str2 += `${(idx + 1).toString().padStart(2, ' ')} : ${oneDesign}\n`;
		}
		console.log(str1);
		console.log(str2);
		console.log('info404: Nothing done!');
	}
}

console.log('make_heliostat.js says Hello!');
await mhcli(process.argv);
console.log('make_heliostat.js says Bye!');

