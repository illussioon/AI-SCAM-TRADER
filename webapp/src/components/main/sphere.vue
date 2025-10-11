<template>
  <div class="sphere-container">
    <canvas 
      ref="canvasRef" 
      class="sphere-canvas"
      :width="canvasWidth" 
      :height="canvasHeight"
    ></canvas>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import * as THREE from 'three'

const canvasRef = ref(null)
const canvasWidth = 828
const canvasHeight = 1152

let scene, camera, renderer, sphere, animationId

onMounted(() => {
  initThreeJS()
  animate()
})

onUnmounted(() => {
  if (animationId) {
    cancelAnimationFrame(animationId)
  }
  if (renderer) {
    renderer.dispose()
  }
})

function initThreeJS() {
  // Создаем сцену
  scene = new THREE.Scene()
  scene.background = new THREE.Color(0x0b0c0d) // Темный фон

  // Создаем камеру
  camera = new THREE.PerspectiveCamera(75, canvasWidth / canvasHeight, 0.1, 1000)
  camera.position.z = 3

  // Создаем рендерер
  renderer = new THREE.WebGLRenderer({
    canvas: canvasRef.value,
    antialias: true,
    alpha: true
  })
  renderer.setSize(canvasWidth, canvasHeight)
  renderer.setPixelRatio(window.devicePixelRatio)

  // Применяем стили к canvas элементу
  canvasRef.value.style.display = 'block'
  canvasRef.value.style.width = '414px'
  canvasRef.value.style.height = '550px'

  // Создаем геометрию сферы (увеличиваем размер)
  const geometry = new THREE.SphereGeometry(1.8, 16, 12) // Увеличили с 1.2 до 1.8
  
  // Создаем wireframe с возможностью настройки толщины
  const wireframeGeometry = new THREE.WireframeGeometry(geometry)
  const material = new THREE.LineBasicMaterial({
    color: 0x29570f, // Темно-зеленый цвет
    transparent: true,
    opacity: 0.9,
    linewidth: 1 // Увеличенная толщина линий
  })

  // Создаем сферу из линий
  sphere = new THREE.LineSegments(wireframeGeometry, material)
  
  // Дополнительный слой для визуально более толстых линий
  const material2 = new THREE.LineBasicMaterial({
    color: 0x29570f,
    transparent: true,
    opacity: 0.4,
    linewidth: 2
  })
  const sphere2 = new THREE.LineSegments(wireframeGeometry.clone(), material2)
  sphere2.scale.set(1.002, 1.002, 1.002) // Чуть больше для эффекта толщины
  
  scene.add(sphere)
  scene.add(sphere2)
  
  // Сохраняем ссылку на второй слой для синхронного вращения
  sphere.userData.sphere2 = sphere2

  // Добавляем небольшое освещение для глубины
  const ambientLight = new THREE.AmbientLight(0x29390d, 0.3)
  scene.add(ambientLight)
}

function animate() {
  animationId = requestAnimationFrame(animate)

  // Вращаем сферу медленнее по часовой стрелке в правую сторону
  if (sphere) {
    sphere.rotation.y += 0.001 // Замедлили с 0.008 до 0.003
    // Синхронизируем вращение второго слоя
    if (sphere.userData.sphere2) {
      sphere.userData.sphere2.rotation.y = sphere.rotation.y
    }
  }

  renderer.render(scene, camera)
}
</script>

<style scoped>
.sphere-container {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  pointer-events: none; /* Отключаем взаимодействие с пользователем */
}

.sphere-canvas {
  display: block;
  width: 414px;
  height: 576px;
  pointer-events: none; /* Отключаем взаимодействие */
  opacity: 0.7;
}

/* Адаптивность */
@media (max-width: 768px) {
  .sphere-canvas {
    width: 350px;
    height: 487px;
  }
}

@media (max-width: 480px) {
  .sphere-canvas {
    display: block;
    width: 380px;
    height: 530px;
  }
}
</style>