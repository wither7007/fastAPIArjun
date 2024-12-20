myUrl = 'http://localhost:8000/'
let gfetch = async (yyy) => {
    let response = await fetch(yyy)
    window.wtext = await response.text()
    console.log(wtext)
}
