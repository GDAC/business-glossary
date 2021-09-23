The styling is creating using a [custom profile](./respec-profile) of [W3C's Respec](https://github.com/w3c/respec) library.

The profile used within the html pages is located in [`respec-gdac.js`](./respec-profile/builds/respec-gdac.js).

If any changes are made to the profile, or to update to include recent respec updates, the profile can be rebuilt using the script below (if you do not have docker you must have `node` available).

```sh
git clone https://github.com/w3c/respec.git
cp -r ./profiles/. ./respec/profiles/
cp -r ./src/. ./respec/src/
cd respec
docker run --rm -v $PWD:/workspace -w /workspace -it node:latest \
/bin/bash -c "npm install . ; node ./tools/builder.js gdac"
cp ./builds/respec-gdac.js ../builds
cp ./builds/respec-gdac.js.map ../builds
cd ..
rm -rf respec
```