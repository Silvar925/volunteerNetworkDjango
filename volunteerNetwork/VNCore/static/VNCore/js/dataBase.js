async function fetchData(url) {
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error(`Ошибка получения данных с сервера: ${response.status}`);
    }
    return response.json();
}

export let news = await fetchData('listNews')
export let events = await fetchData('listEvents')
export let speaker = await fetchData('listSpeakers')
export let organizer = await fetchData('listOrganizers')
export let rating = await fetchData('listRating')