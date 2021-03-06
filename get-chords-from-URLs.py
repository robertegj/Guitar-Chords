import time
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# Insert your own URLs, these are for educational purposes only

bookmarkURLs = ["http://tabs.ultimate-guitar.com/b/beatles/eleanor_rigby_ver2_crd.htm",
"https://tabs.ultimate-guitar.com/tab/weezer/hash-pipe-chords-1009559",
"http://tabs.ultimate-guitar.com/s/system_of_a_down/lonely_day_ver2_crd.htm",
"http://www.guitaretab.com/s/system-of-a-down/256124.html",
"http://www.azlyrics.com/lyrics/systemofadown/aerials.html",
"https://www.google.com/search?q=diy+lps+devil+costume&espv=2&tbm=isch&tbo=u&source=univ&sa=X&ei=rLHuU4rmMcrJ8AHYuYGoDw&ved=0CBwQsAQ&biw=1920&bih=955#q=diy%20lps%20costume&tbm=isch&facrc=_&imgdii=ZyAGwH6Jk2ONCM%3A%3Bh6UeMLsZ45XAGM%3BZyAGwH6Jk2ONCM%3A&imgrc=ZyAGwH6Jk2ONCM%253A%3BJCyY0fR-8eC4YM%3Bhttp%253A%252F%252Fi1.squidoocdn.com%252Fresize%252Fsquidoo_images%252F400%252Fdraft_lens1847374module8176342photo_1249837803cat_littlest_pet_shop_vip.jpg%3Bhttp%253A%252F%252Fwww.squidoo.com%252FLittlestpetshopvips%3B250%3B250",
"http://tabs.ultimate-guitar.com/s/system_of_a_down/roulette_crd.htm",
"https://www.youtube.com/watch?v=-ydwG1PT2Yk",
"http://tabs.ultimate-guitar.com/s/system_of_a_down/atwa_ver13_tab.htm",
"https://www.youtube.com/watch?v=gzKCgwvv-vw",
"http://tabs.ultimate-guitar.com/s/system_of_a_down/atwa_ver2_crd.htm",
"http://tabs.ultimate-guitar.com/s/system_of_a_down/aerials_tab.htm",
"https://tabs.ultimate-guitar.com/d/drake/the_motion_crd.htm",
"https://tabs.ultimate-guitar.com/s/simon_garfunkel/sound_of_silence_ver4_crd.htm",
"https://tabs.ultimate-guitar.com/h/hozier/take_me_to_church_ver5_crd.htm",
"https://tabs.ultimate-guitar.com/m/misc_soundtrack/jesus_christ_superstar_-_pilates_dream_crd.htm",
"https://tabs.ultimate-guitar.com/l/leonard_cohen/hallelujah_ver6_crd.htm",
"https://tabs.ultimate-guitar.com/n/nirvana/where_did_you_sleep_last_night_ver2_crd.htm",
"https://tabs.ultimate-guitar.com/l/leonard_cohen/hallelujah_ver2_crd.htm",
"https://tabs.ultimate-guitar.com/b/bill_withers/aint_no_sunshine_ver2_crd.htm",
"https://tabs.ultimate-guitar.com/tab/weezer/say_it_aint_so_chords_1911611",
"https://tabs.ultimate-guitar.com/x/xxxtentacion/garettes_revenge_ver3_crd.htm",
"https://tabs.ultimate-guitar.com/tab/1995699",
"https://tabs.ultimate-guitar.com/tab/j_cole/kevins_heart_chords_2375239",
"https://tabs.ultimate-guitar.com/tab/nirvana/lithium-chords-1119299",
"https://tabs.ultimate-guitar.com/tab/eve-6/inside-out-chords-1105574",
"https://tabs.ultimate-guitar.com/tab/cake/sheep-go-to-heaven-chords-1489383",
"https://tabs.ultimate-guitar.com/tab/john-lennon/imagine-chords-9306",
"https://tabs.ultimate-guitar.com/tab/violent-femmes/blister-in-the-sun-chords-1748968",
"https://tabs.ultimate-guitar.com/tab/sublime/summertime-doin-time-chords-2208049",
"https://tabs.ultimate-guitar.com/tab/camila-cabello/havana-chords-2105155",
"https://tabs.ultimate-guitar.com/tab/green-day/good-riddance-time-of-your-life-chords-12835",
"https://tabs.ultimate-guitar.com/tab/sublime/what-i-got-chords-2553",
"https://tabs.ultimate-guitar.com/tab/eurythmics/sweet-dreams-are-made-of-this-chords-1203755",
"https://tabs.ultimate-guitar.com/tab/cake/friend-is-a-four-letter-word-chords-350209",
"https://tabs.ultimate-guitar.com/tab/cake/perhaps-perhaps-perhaps-chords-63320",
"https://tabs.ultimate-guitar.com/tab/pixies/where-is-my-mind-chords-89446",
"https://tabs.ultimate-guitar.com/tab/nirvana/polly-chords-832979",
"https://tabs.ultimate-guitar.com/tab/nirvana/heart-shaped-box-chords-1399119",
"https://tabs.ultimate-guitar.com/tab/the-cure/boys-dont-cry-chords-956417",
"https://tabs.ultimate-guitar.com/tab/weezer/all-my-favorite-songs-chords-3525851",
"https://tabs.ultimate-guitar.com/tab/3732140",
"https://tabs.ultimate-guitar.com/tab/nirvana/rape-me-chords-841026",
"https://tabs.ultimate-guitar.com/tab/blink-182/all-the-small-things-chords-118610",
"https://tabs.ultimate-guitar.com/tab/system-of-a-down/atwa-chords-1096241",
"https://tabs.ultimate-guitar.com/tab/system-of-a-down/hypnotize-chords-1877036",
"https://tabs.ultimate-guitar.com/tab/system-of-a-down/hypnotize-tabs-261780",
"https://tabs.ultimate-guitar.com/tab/system-of-a-down/lost-in-hollywood-chords-967895",
"https://tabs.ultimate-guitar.com/tab/system-of-a-down/lost-in-hollywood-chords-2529570",
"https://soundcloud.com/rabbirt",
"https://tabs.ultimate-guitar.com/tab/clairo/pretty-girl-chords-2114217",
"https://tabs.ultimate-guitar.com/tab/billie-eilish/everything-i-wanted-chords-2892650",
"https://tabs.ultimate-guitar.com/tab/the-rolling-stones/paint-it-black-chords-606572",
"https://tabs.ultimate-guitar.com/tab/pink-floyd/breathe-chords-1418240",
"https://tabs.ultimate-guitar.com/tab/sex-bob-omb/garbage-truck-chords-1011179",
"https://tabs.ultimate-guitar.com/tab/nirvana/the-man-who-sold-the-world-chords-841325",
"https://tabs.ultimate-guitar.com/tab/the-rolling-stones/drift-away-chords-1977687",
"https://tabs.ultimate-guitar.com/tab/sublime/wrong-way-chords-83374",
"https://tabs.ultimate-guitar.com/tab/sohodolls/bang-bang-bang-bang-chords-3403979",
"https://tabs.ultimate-guitar.com/tab/tom-petty-and-the-heartbreakers/mary-janes-last-dance-chords-205804",
"https://tabs.ultimate-guitar.com/tab/jet/cold-hard-bitch-chords-1949745",
"https://tabs.ultimate-guitar.com/tab/jet/are-you-gonna-be-my-girl-chords-1058317",
"https://tabs.ultimate-guitar.com/tab/franz-ferdinand/take-me-out-chords-176648",
"https://tabs.ultimate-guitar.com/tab/green-day/american-idiot-chords-145586",
"https://tabs.ultimate-guitar.com/tab/the-offspring/self-esteem-chords-1066243",
"https://tabs.ultimate-guitar.com/tab/red-hot-chili-peppers/under-the-bridge-chords-44981",
"https://tabs.ultimate-guitar.com/tab/olivia-rodrigo/jealousy-jealousy-chords-3717647",
"https://tabs.ultimate-guitar.com/tab/milky-chance/colorado-chords-3756701",
"https://tabs.ultimate-guitar.com/tab/the-offspring/the-kids-arent-alright-chords-844306",
"https://tabs.ultimate-guitar.com/tab/sum-41/still-waiting-chords-193628",
"https://tabs.ultimate-guitar.com/tab/red-hot-chili-peppers/by-the-way-chords-954593",
"https://tabs.ultimate-guitar.com/tab/simon-garfunkel/the-sound-of-silence-chords-159157",
"https://tabs.ultimate-guitar.com/tab/blur/song-2-chords-1508087",
"https://tabs.ultimate-guitar.com/tab/stone-temple-pilots/creep-chords-44309",
"https://tabs.ultimate-guitar.com/tab/the-offspring/hit-that-chords-761432",
"https://tabs.ultimate-guitar.com/tab/foo-fighters/something-from-nothing-chords-1672116",
"https://tabs.ultimate-guitar.com/tab/foo-fighters/all-my-life-chords-386918",
"https://tabs.ultimate-guitar.com/tab/t-a-t-u-/all-the-things-she-said-chords-2402315",
"https://chordseasy.com/song/33119/never-gonna-give-you-up",
"https://tabs.ultimate-guitar.com/tab/yungblud/fleabag-chords-3840632",
"https://tabs.ultimate-guitar.com/tab/tessa-violet/crush-chords-2404553",
"https://tabs.ultimate-guitar.com/tab/gorillaz/tranz-chords-2409029",
"https://tabs.ultimate-guitar.com/tab/audioslave/be-yourself-chords-608448",
"https://www.guitaretab.com/a/audioslave/363202.html",
"https://tabs.ultimate-guitar.com/tab/stone-temple-pilots/plush-chords-1833407",
"https://tabs.ultimate-guitar.com/tab/modest-mouse/float-on-chords-587814",
"https://tabs.ultimate-guitar.com/tab/beck/loser-chords-3575723",
"https://tabs.ultimate-guitar.com/tab/misc-cartoons/encanto-we-dont-talk-about-bruno-chords-3956839",
"https://tabs.ultimate-guitar.com/tab/super-deluxe/alex-jones-folk-song-chords-2086367",
"https://tabs.ultimate-guitar.com/tab/xxxtentacion/revenge-chords-2001755",
"https://tabs.ultimate-guitar.com/tab/cake/frank-sinatra-chords-868901",
"https://tabs.ultimate-guitar.com/tab/weezer/island-in-the-sun-chords-852868",
"https://tabs.ultimate-guitar.com/tab/oasis/wonderwall-chords-27596",
"https://tabs.ultimate-guitar.com/tab/cage-the-elephant/cold-cold-cold-chords-1797459",
"https://tabs.ultimate-guitar.com/tab/blink-182/whats-my-age-again-chords-1173080",
"https://tabs.ultimate-guitar.com/tab/graduating-life/stinky-man-chords-3752654",
"https://tabs.ultimate-guitar.com/tab/red-hot-chili-peppers/snow-hey-oh-chords-497382",
"https://tabs.ultimate-guitar.com/tab/the-animals/house-of-the-rising-sun-chords-18688",
"https://tabs.ultimate-guitar.com/tab/gorillaz/feel-good-inc-chords-1434111",
"https://tabs.ultimate-guitar.com/tab/gorillaz/on-melancholy-hill-chords-929606",
"https://tabs.ultimate-guitar.com/tab/nirvana/dumb-chords-907179",
"https://tabs.ultimate-guitar.com/tab/lit/my-own-worst-enemy-chords-950238",
"https://tabs.ultimate-guitar.com/tab/ansel-elgort/supernova-chords-2283837",
"https://tabs.ultimate-guitar.com/tab/sushi-soucy/i-deserve-to-bleed-chords-3600911",
"https://tabs.ultimate-guitar.com/tab/3357074",
"https://tabs.ultimate-guitar.com/tab/465291"]

for bookmarkURL in bookmarkURLs:
    print("getting: "+bookmarkURL)
    driver.get(bookmarkURL)
    time.sleep(5)
    if "Oops!" in driver.title:
        print("Expired")
        continue
    n=driver.title+'.txt'
    re.sub(' .*(.Com)','',n)
    try:
        chordElem = driver.find_element(By.XPATH, "//pre")
    except:
        continue
    with open(n, 'w') as f:
        f.write(chordElem.text)

