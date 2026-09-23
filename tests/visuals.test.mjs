import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {visuals,visualStage,demoArts,art} from '../public/visuals.js';
const plan=JSON.parse(await fs.readFile('public/curriculum.json','utf8'));
test('each teaching station has three selectable visual frames and own-account practice',()=>{
 for(const l of plan.lessons){const v=visuals[l.id];assert.ok(v);assert.equal(v.steps.length,3);assert.equal(v.frames.length,3);assert.equal(v.do.length,3);const html=visualStage(l.id);assert.equal((html.match(/data-frame-select=/g)||[]).length,3);assert.equal((html.match(/data-frame-panel=/g)||[]).length,3);assert.match(html,/keine Live-Abfrage/);assert.match(html,/data-play/);for(const f of v.frames)assert.ok(art(f[1],f[2]).length>100);}
});
test('research and browser actions are distinct stations',()=>{
 const research=plan.lessons.find(x=>x.id==='recherche'),browser=plan.lessons.find(x=>x.id==='browser');
 assert.match(JSON.stringify(research),/Teherani/);assert.match(JSON.stringify(browser),/Filter/);assert.match(JSON.stringify(browser),/In-App-Browser/);assert.equal(demoArts.browser.length,browser.demos.length);
});
