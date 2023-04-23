const noOfLights = 16
const lightBtns = document.getElementsByClassName("light-button")

const setLights = (lStr) => {
    for (let i = 0; i < noOfLights; i++) {
        lightBtns[i].style.background = (lStr[i] == "1") ? "yellow" : "white"
    }
}

const lightChoice = async (btn, value) => {
    // console.log(`Button ${value}`)
    setLights(await eel.lightPress(value)())
}