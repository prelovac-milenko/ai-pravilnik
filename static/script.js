document.addEventListener('DOMContentLoaded', function() {
  // Update file info when files are selected
  const fileUpload = document.getElementById('file-upload');
  const fileInfo = document.querySelector('.file-info');
  
  if (fileUpload && fileInfo) {
    fileUpload.addEventListener('change', function() {
      if (this.files.length > 0) {
        if (this.files.length === 1) {
          fileInfo.textContent = this.files[0].name;
        } else {
          fileInfo.textContent = `${this.files.length} fajlova izabrano`;
        }
      } else {
        fileInfo.textContent = 'Nema dodatih fajlova';
      }
    });
  }

  // Copy answer to clipboard
  const copyButtons = document.querySelectorAll('.action-btn:first-child');
  copyButtons.forEach(button => {
    button.addEventListener('click', function() {
      const answerContent = this.closest('.answer-section').querySelector('.answer-content').textContent;
      navigator.clipboard.writeText(answerContent.trim())
        .then(() => {
          const originalText = this.innerHTML;
          this.innerHTML = '<i class="fas fa-check"></i> Kopirano!';
          setTimeout(() => {
            this.innerHTML = originalText;
          }, 2000);
        })
        .catch(err => {
          console.error('Failed to copy text: ', err);
        });
    });
  });

  // Add loader functionality
  const askForm = document.querySelector('.ask-form');
  const loadingContainer = document.querySelector('.loading-container');
  const answerSection = document.querySelector('.answer-section');
  const loadingText = document.querySelector('.loading-text');

  if (askForm && loadingContainer) {
    askForm.addEventListener('submit', function() {
      // Hide previous answer if exists
      if (answerSection) answerSection.classList.add('hidden');
      
      // Show loading animation
      loadingContainer.classList.remove('hidden');
      
      // Scroll to loader
      loadingContainer.scrollIntoView({ behavior: 'smooth', block: 'center' });
      
      // Change text dynamically
      const steps = [
        
      ];
      
      let currentStep = 0;
      const textInterval = setInterval(() => {
        loadingText.textContent = steps[currentStep];
        currentStep = (currentStep + 1) % steps.length;
      }, 2000);
      
      // Clear interval when form submits (page reloads)
      // This happens automatically when the form submits
    });
  }
});