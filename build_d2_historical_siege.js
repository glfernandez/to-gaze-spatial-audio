const { execSync } = require('child_process');

console.log('=== Building 1240 AD Historical Siege Soundscape for Scene D2 ===');
console.log('(Pure Medieval Acoustic Foley — Zero Gunfire, Zero Modern War Artifacts)');

execSync('python3 scripts/build_clean_d2_siege.py', { stdio: 'inherit' });
console.log('✓ All 9 D2 siege takes successfully generated.');
