#!/usr/bin/env node
// make_heliostat.js

import { exec } from "child_process";
import { promisify } from 'util';

const c_Parts = {
	heliostat: 'heliostat_v01',
	heliostat_2: 'heliostat_2_v01',
	base: 'base_v01',
	pole_static: 'pole_static_v01',
	pole_rotor: 'pole_rotor_v01',
	rake: 'rake_v01',
	rake_stopper: 'rake_stopper_v01',
	spider: 'spider_v01',
	swing: 'swing_v01',
	rod: 'rod_v01',
	trapeze: 'trapeze_v01',
	surface: 'surface_v01'
};

function getCmd(dName, fName) {
	const rCmd = [];
	//rCmd.push('pwd');
	//rCmd.push(`ls ${dName}`);
	//rCmd.push(`npx designix -d=heliostat/${dName} -o=${dName} --outFileName=px_${fName}.json write json_param`);
	rCmd.push(`npx designix -d=heliostat/${dName} -p=${dName}/px_${fName}.json -o=${dName} --outFileName=${fName}.scad write scad_3d_openscad`);
	rCmd.push(`openscad -o ${dName}/${fName}.stl ${dName}/${fName}.scad`);
	//rCmd.push(`npx shx rm -fr ${dName}`);
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

