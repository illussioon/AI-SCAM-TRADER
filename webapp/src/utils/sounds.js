// Утилита для проигрывания звуков
export const playSound = (soundPath, volume = 0.5) => {
  try {
    const audio = new Audio(soundPath)
    audio.volume = volume
    audio.play().catch(e => {
      console.log('Не удалось воспроизвести звук:', e)
    })
  } catch (error) {
    console.log('Ошибка при загрузке звука:', error)
  }
}

// Предустановленные звуки
export const sounds = {
  click: '/sound/click.mp3'
}

// Специализированная функция для звука клика
export const playClickSound = (volume = 0.5) => {
  playSound(sounds.click, volume)
}
