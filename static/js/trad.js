console.log("Translate script called.")

// API constants
const deepLURL = 'https://api-free.deepl.com/v2/translate'
const deepLKey = 'DeepL-Auth-Key 9b267d6b-166b-e365-0c72-8a1c7563d476:fx'

// Get all elements that need to be translated and the target language
const targetLanguage = document.getElementsByClassName("hidden-lang")[0].classList[0]
const toBeTranslated = document.getElementsByClassName("translate");
let translated = [];

for (var i = 0; i < toBeTranslated.length; i++)
{
    fetch(deepLURL, {
        mode: 'cors',
        method: 'POST',
        headers: {
            'Authorization': deepLKey,
            'Content-Type': 'x-www-form-urlencoded',
            'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify({
            "text": encodeURI(toBeTranslated[i].textContent),
            'target_lang': targetLanguage
        })
    })
        .then(response => response.json())
        .then(response => {
            const translatedResource = response["translations"]["text"];
            translated.push(translatedResource);
        });
    
    document.getElementsByClassName('translate')[i].textContent = translated[i];
};