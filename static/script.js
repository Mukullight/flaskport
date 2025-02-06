import { GLTFLoader } from "https://cdn.skypack.dev/three@0.129.0/examples/jsm/loaders/GLTFLoader.js";

const loader = new GLTFLoader();
// Using Flask's url_for to reference the glTF file
loader.load('/static/cube.gltf', function (gltf) {
  scene.add(gltf.scene);
}, undefined, function (error) {
  console.error(error);
});

