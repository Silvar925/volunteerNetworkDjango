export function getAllTagsA(id) {
    let arrayA = []
    let myDiv = document.getElementById(id);
    let linksInsideDiv = myDiv.getElementsByTagName("a");

    for (let i = 0; i < linksInsideDiv.length; i++) {
        arrayA.push(linksInsideDiv[i])
    }

    return arrayA
}

export function extractNumbersFromString(inputString) {
    const matches = inputString.match(/\d+/);

    if (matches) {
        return parseInt(matches[0], 10);
    } else {
        return null;
    }
}

export function clearDiv(div) {
    var divElement = document.getElementById(div); // Replace 'yourDivId' with the actual ID of your div
    if (divElement) {
        divElement.innerHTML = ''; // Set the inner HTML content of the div to an empty string
    } else {
        console.error('Div not found!'); // Log an error if the div with the specified ID is not found
    }
}  