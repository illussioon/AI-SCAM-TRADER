// Утилита для воспроизведения звуков
export function playClickSound() {
  try {
    const audio = new Audio('/sound/click.mp3')
    audio.volume = 0.5 // Устанавливаем громкость 50%
    audio.play().catch(error => {
      console.warn('Не удалось воспроизвести звук клика:', error)
    })
  } catch (error) {
    console.warn('Ошибка при создании аудио элемента:', error)
  }
}

export function playSound(soundPath, volume = 0.5) {
  try {
    const audio = new Audio(soundPath)
    audio.volume = volume
    audio.play().catch(error => {
      console.warn(`Не удалось воспроизвести звук ${soundPath}:`, error)
    })
  } catch (error) {
    console.warn('Ошибка при создании аудио элемента:', error)
  }
}
