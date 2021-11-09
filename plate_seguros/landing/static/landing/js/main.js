const sections = ['home', 'quienesSomos',  'seguros', 'incapacidad','contacto'];

function getElementPositionById(elementId) {
  const element = document.getElementById(elementId);
  if (element) {
    const rect = element.getBoundingClientRect(),
    scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    return rect.top + scrollTop - 1;
  }
  return false;
}

function getSectionsPositions() {
  let sectionsPositions = [];
  sections.forEach(function(section) {
    const position = getElementPositionById(section);
    const el = document.getElementById(section);
    if (el) {
      const offsetHeight = el.offsetHeight;
      sectionsPositions.push({name: section, position: position, offsetHeight: offsetHeight});
    }
  });
  return sectionsPositions;
}

function getSectionInViewport() {
  const currentScrollPosition = window.pageYOffset || document.documentElement.scrollTop;
  const sections = getSectionsPositions();
  let currentSectionInViewport = '';
  sections.forEach(function(section) {
    if ((section.position <= currentScrollPosition) &&
        (currentScrollPosition < (section.position + section.offsetHeight))) {
      currentSectionInViewport = section.name;
    }
  });
  return currentSectionInViewport;
}

function menuArrows() {
  const arrowUp = document.getElementById('menuArrowUp');
  const arrowDown = document.getElementById('menuArrowDown');
  const sectionsPositions = getSectionsPositions();

  if (arrowUp) {
    arrowUp.addEventListener('click', function() {
      const currentSection = getSectionInViewport();
      const sectionIndex = sections.findIndex(function(el) { return el === currentSection });
      if (sectionIndex > 0) {
        // window.scrollTo(0, sectionsPositions[sectionIndex - 1].position + 1);
        location.hash = "#" + sectionsPositions[sectionIndex - 1].name;
      }
    });
  }
  
  if (arrowDown) {
    arrowDown.addEventListener('click', function() {
      const currentSection = getSectionInViewport();
      const sectionIndex = sections.findIndex(function(el) { return el === currentSection });
      if (sectionIndex < 4) {
        // window.scrollTo(0, sectionsPositions[sectionIndex + 1].position + 1);
        location.hash = "#" + sectionsPositions[sectionIndex + 1].name;
      }
    });
  }
}

function activeMenuItem() {
  const sectionInViewport = getSectionInViewport();
  const menuItemId = 'menuItem_' + sectionInViewport;
  const activeMenuItemElement = document.getElementById(menuItemId);
  const menuItems = document.querySelectorAll('#menu ul li a');
  menuItems.forEach(function(item) {
    item.classList.remove('active');
  });
  if (activeMenuItemElement) {
    activeMenuItemElement.classList.add('active');
  }
}


function changeMenuColor() {
  const menuItems = document.querySelectorAll('#menu ul li');
  const scrollY = window.scrollY;
  const quienesSomosPosition = getElementPositionById('quienesSomos');
  const contactoPosition = getElementPositionById('contacto');
  if(quienesSomosPosition && scrollY >= quienesSomosPosition && (contactoPosition && scrollY < contactoPosition)) {
    menuItems.forEach(function(el) {
      el.classList.add('dark');
    })
  }
  else if (contactoPosition && scrollY >= contactoPosition) {
    menuItems.forEach(function(el) {
      el.classList.remove('dark');
    })
  } else {
    menuItems.forEach(function(el) {
      el.classList.remove('dark');
    })
  }
}

function hideOrShowMenuLabels() {
  const scrollY = window.scrollY;
  const menu = document.getElementById('menu');
  if (menu) {
    if(scrollY > 0) {
      menu.classList.add('hidden-labels');
    } else {
      menu.classList.remove('hidden-labels');
    }
  }
}

document.addEventListener('scroll', function(e) {
  changeMenuColor();
  hideOrShowMenuLabels();
  activeMenuItem();
});

changeMenuColor();
hideOrShowMenuLabels();

function showAseguradorasSlider() {
  const aseguradorasSlider = $('#aseguradorasSlider');
  if (window.innerWidth <= 600) {
    try {
      const aseguradorasSlick = aseguradorasSlider.slick('getSlick');
      if(aseguradorasSlick) {
        aseguradorasSlider.slick('init');
      }
    } catch (err) {
      console.log(err);
      aseguradorasSlider.slick({
        dots: true,
        rows: 5,
        slidesPerRow: 2,
        appendArrows: '.aseguradoras-slider-nav',
        appendDots: '.aseguradoras-slider-nav',
        prevArrow: '<button type="button" class="slick-prev"><svg width="8" height="14" viewBox="0 0 8 14" fill="none" xmlns="http://www.w3.org/2000/svg">\n' +
        '<path d="M7.14288 1L2.00003 7.09326L7.14288 13" stroke="#3A445D" stroke-width="2"/>\n' +
        '</svg>\n</button>',
        nextArrow: '<button type="button" class="slick-next"><svg width="8" height="14" viewBox="0 0 8 14" fill="none" xmlns="http://www.w3.org/2000/svg">\n' +
        '<path d="M1 13L6.14286 6.90674L0.999999 1" stroke="#3A445D" stroke-width="2"/>\n' +
        '</svg>\n</button>',
        customPaging : function(slider, i) {
          return '<button><svg class="circle" width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">\n' +
          '<circle cx="6" cy="6" r="5" stroke="#3A445D" stroke-width="2"/></svg></button>';
        },
      });
    }
  } else {
    try {
      const aseguradorasSlick = aseguradorasSlider.slick('getSlick');
      if(aseguradorasSlick) {
        aseguradorasSlider.slick('unslick');
      }
    } catch (err) {
      console.log(err);
    }
  }
}


// TODO change slider on resize, use unslick?
function showSegurosSlider() {
  const segurosGrid = $('#segurosGrid');
  if (window.innerWidth <= 600) {
    try {
      const segurosSlick = segurosGrid.slick('getSlick');
      if(segurosSlick) {
        segurosGrid.slick('init');
      }
    } catch (err) {
      console.log(err);
      segurosGrid.slick({
        centerMode: true,
        dots: true,
        centerPadding: '30px',
        infinite: false,
        appendArrows: '.seguros-slider-nav',
        appendDots: '.seguros-slider-nav',
        prevArrow: '<button type="button" class="slick-prev"><svg width="8" height="14" viewBox="0 0 8 14" fill="none" xmlns="http://www.w3.org/2000/svg">\n' +
        '<path d="M7.14288 1L2.00003 7.09326L7.14288 13" stroke="#3A445D" stroke-width="2"/>\n' +
        '</svg>\n</button>',
        nextArrow: '<button type="button" class="slick-next"><svg width="8" height="14" viewBox="0 0 8 14" fill="none" xmlns="http://www.w3.org/2000/svg">\n' +
        '<path d="M1 13L6.14286 6.90674L0.999999 1" stroke="#3A445D" stroke-width="2"/>\n' +
        '</svg>\n</button>',
        customPaging : function(slider, i) {
          return '<button><svg class="circle" width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">\n' +
          '<circle cx="6" cy="6" r="5" stroke="#3A445D" stroke-width="2"/></svg></button>';
        },
      });
    }
  } else {
    try {
      const segurosSlick = segurosGrid.slick('getSlick');
      if(segurosSlick) {
        segurosGrid.slick('unslick');
      }
    } catch (err) {
      console.log(err);
    }
  }
}

function showIncapacidadSlider() {
  $('#sliderIncapacidad').slick({
    dots: true,
    appendDots: '.incapacidad-slider-nav',
    customPaging : function(slider, i) {
      return '<button><svg class="circle" width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">\n' +
      '<circle cx="6" cy="6" r="5" stroke="#3A445D" stroke-width="2"/></svg></button>';
    },
    prevArrow: '<button class="slick-prev"><svg width="41" height="79" viewBox="0 0 41 79" fill="none" xmlns="http://www.w3.org/2000/svg">\n' +
    '<g filter="url(#filter0_d)">\n' +
    '<path d="M36 1L5.99999 36.0363L36 70" stroke="#3A445D" stroke-width="2"/>\n' +
    '</g>\n' +
    '<defs>\n' +
    '<filter id="filter0_d" x="0.674805" y="0.349609" width="40.0848" height="78.3124" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">\n' +
    '<feFlood flood-opacity="0" result="BackgroundImageFix"/>\n' +
    '<feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>\n' +
    '<feOffset dy="4"/>\n' +
    '<feGaussianBlur stdDeviation="2"/>\n' +
    '<feComposite in2="hardAlpha" operator="out"/>\n' +
    '<feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"/>\n' +
    '<feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow"/>\n' +
    '<feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow" result="shape"/>\n' +
    '</filter>\n' +
    '</defs>\n' +
    '</svg>\n</button>',
    nextArrow: '<button class="slick-next"><svg width="41" height="79" viewBox="0 0 41 79" fill="none" xmlns="http://www.w3.org/2000/svg">\n' +
    '<g filter="url(#filter0_d)">\n' +
    '<path d="M5 70L35 34.9637L5 1" stroke="#3A445D" stroke-width="2"/>\n' +
    '</g>\n' +
    '<defs>\n' +
    '<filter id="filter0_d" x="0.240356" y="0.337891" width="40.0848" height="78.3124" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">\n' +
    '<feFlood flood-opacity="0" result="BackgroundImageFix"/>\n' +
    '<feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>\n' +
    '<feOffset dy="4"/>\n' +
    '<feGaussianBlur stdDeviation="2"/>\n' +
    '<feComposite in2="hardAlpha" operator="out"/>\n' +
    '<feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"/>\n' +
    '<feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow"/>\n' +
    '<feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow" result="shape"/>\n' +
    '</filter>\n' +
    '</defs>\n' +
    '</svg>\n</button>'
  });
}


$(document).ready(function(){
  activeMenuItem();
  menuArrows();
});

$(window).on('load', function() {
  showSegurosSlider();
  showIncapacidadSlider();
  // showAseguradorasSlider();
  AOS.init();
});

window.addEventListener('resize', function() {
  showSegurosSlider();
  // showAseguradorasSlider();
});




// Mobile menu open
const mobileMenuBurger = document.getElementById('mobileMenuBurger');
const mobileMenuOpen = document.getElementById('mobileMenuOpen');
const mobileMenuCloseButton = document.getElementById('mobileMenuCloseButton');
const mobileMenuItems = document.querySelectorAll('#mobileMenuOpen .list li a');
const mobileMenuContactoButton = document.querySelector('#mobileMenuOpen .button a')

if (mobileMenuBurger) {
  mobileMenuBurger.addEventListener('click', function() {
    if(!mobileMenuOpen.classList.contains('open')) {
      mobileMenuOpen.classList.add('open');
    }
    const sectionInViewport = getSectionInViewport();
    const menuItemToActivate = document.getElementById('mobileMenuItem_' + sectionInViewport);
    mobileMenuItems.forEach(function(el) {
      el.classList.remove('active');
    });
    if (menuItemToActivate) {
      menuItemToActivate.classList.add('active');
    }
  });
}

if (mobileMenuCloseButton) {
  mobileMenuCloseButton.addEventListener('click', function() {
    if(mobileMenuOpen.classList.contains('open')) {
      mobileMenuOpen.classList.remove('open');
    }
  });
}

if (mobileMenuContactoButton) {
  mobileMenuContactoButton.addEventListener('click', function() {
    if(mobileMenuOpen.classList.contains('open')) {
      mobileMenuOpen.classList.remove('open');
    }
  });
}

if (mobileMenuItems) {
  mobileMenuItems.forEach(function(el) {
    el.addEventListener('click', function() {
      if(mobileMenuOpen.classList.contains('open')) {
        mobileMenuOpen.classList.remove('open');
      }
    });
  });
}

