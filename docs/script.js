// preload images
const images = ['images/bounce/1_1.png', 'images/bounce/1_2.png', 'images/bounce/2_1.png', 'images/bounce/2_2.png', 'images/bounce/3_1.png', 'images/bounce/3_2.png', 'images/bounce/4_1.png', 'images/bounce/4_2.png', 'images/jump/1_1.png', 'images/jump/1_2.png', 'images/jump/2_1.png', 'images/jump/2_2.png', 'images/jump/3_1.png', 'images/jump/3_2.png', 'images/omok/1_1.png', 'images/omok/1_2.png', 'images/omok/2_1.png', 'images/omok/2_2.png', 'images/omok/3_1.png', 'images/omok/3_2.png', 'images/omok/4_1.png', 'images/omok/4_2.png', 'images/omok/5_1.png', 'images/omok/5_2.png'];
let loadedImages = [];
for (let i = 0; i < images.length; i++) {
    loadedImages[i] = new Image();
    loadedImages[i].src = images[i];
}

// section color themes
const themes = {
    'omok': [
        {
            'background-color': '#e1b954',
            'color': '#000000',
        },
        {
            'background-color': '#afb8b3',
            'color': '#174a45',
        },
        {
            'background-color': '#292929',
            'color': '#d7d7d7',
        },
        {
            'background-color': '#4d857c',
            'color': '#e1ddbf',
        },
        {
            'background-color': '#793937',
            'color': '#f1ad88',
        },
        {
            'background-color': '#997787',
            'color': '#fdd8be',
        },
    ],
    'bounce': [
        {
            'background-color': '#2f6262',
            'color': '#afb9b4',
        },
        {
            'background-color': '#d1cfb8',
            'color': '#4c837a',
        },
        {
            'background-color': '#e6c0a8',
            'color': '#997787',
        },
        {
            'background-color': '#fcc6a9',
            'color': '#793937',
        },
        {
            'background-color': '#141414',
            'color': '#d7d7d7',
        },
    ],
    'jump': [
        {
            'background-color': '#80a6a0',
            'color': '#e1ddbf',
        },
        {
            'background-color': '#e3afb1',
            'color': '#fcecec',
        },
        {
            'background-color': '#808ea6',
            'color': '#bfcfe1',
        },
        {
            'background-color': '#646464',
            'color': '#b4b4b4',
        },
    ],
};
let themeIndex = {
    'omok': 0,
    'bounce': 0,
    'jump': 0,
};
function changeTheme(section) {
    themeIndex[section]++;
    if (themeIndex[section] >= Object.keys(themes[section]).length) {
        themeIndex[section] = 0;
    }

    document.getElementById(`${section}1`).src = `images/${section}/${themeIndex[section]}_1.png`;
    document.getElementById(`${section}2`).src = `images/${section}/${themeIndex[section]}_2.png`;
    document.getElementById(section).style.backgroundColor = themes[section][themeIndex[section]]['background-color'];
    document.getElementById(section).style.color = themes[section][themeIndex[section]]['color'];
}