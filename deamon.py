import apikey
import random
import discord

client = discord.Client()

@client.event
async def on_ready():
  print("logged in as " + client.user.name)

@client.event
async def on_message(message):
  if message.author != client.user:
#      if "ラーメン占い" in message.content:
      if message.content.startswith("ラーメン占い"):
        num = random.randint(0,100)

        if num < 4:
          shop_title = "松戸二郎"
          msg = "このまえ久しぶりに訪問したらうますぎてびびったね。\n"
          msg += "乳化の濃いスープにデロ麺、キャベツ多め、でかやわ豚3個、豚カス入りアブラと最高で笑ってしまった\n"
          msg += "量も思ったより？は多くなくてちょうどいいくらい\n"
          msg += "小ラーメンアブラカラメ、どうですか"
          ramen_url = "https://pbs.twimg.com/media/EVULba5VAAAYQa0?format=jpg&name=large"

        elif 4 <= num < 8:
          shop_title = "雨ニモマケズ　十条"
          msg = "スパイシーガーリックオイルまぜそば\n"
          msg += "スパイシーが強めでカレー風味？のまぜそば。麺がうまかった。"
          msg += "特製鶏白湯つけ麺\n"
          msg += "粘度のあるスープだが軽めで飲みやすいスープ。優しめ"
          ramen_url = "https://pbs.twimg.com/media/EVKbFujUMAEqMhA?format=jpg&name=large"
          ramen_url2 = "https://pbs.twimg.com/media/EVKbFuhUcAIoXVF?format=jpg&name=large"
          ramen_url3 = "https://pbs.twimg.com/media/EVKbF_4VAAYWyKE?format=jpg&name=large"

        elif 8 <= num < 12: 
          shop_title = "ラーメン　英二　北府中"
          msg = "久しぶりのラーメン。\n"
          msg += "スープもっと粘度があった記憶だったが、さらさらで味も薄めだった感。\n"
          msg += "豚はホロホロだが少しパサメ。\n"
          msg += "別皿アブラが味めっちゃ濃くて最高ね\n"
          msg += "ラーメンヤサイチョイマシアブラカラメ。"
          ramen_url = "https://pbs.twimg.com/media/EVKaRYUUEAEXJZy?format=jpg&name=large"

        elif 12 <= num < 16: 
          shop_title = "すぎ本"
          msg = "特製醤油らぁ麺＋チャーシューご飯\n"
          msg += "前から食べたかった店。初来訪\n"
          msg += "様々な味のするとても優しいスープ。とにかくやさしい。\n"
          msg += "トッピングも美味しい。チャーシュー丼もたっぷりの肉としっかり味がついており良さ"
          ramen_url = "https://pbs.twimg.com/media/EVKbFuhUcAIoXVF?format=jpg&name=large"
          ramen_url2 = "https://pbs.twimg.com/media/EVKZuCuU8AAs3Xx?format=jpg&name=large"

        elif 16 <= num < 20: 
          shop_title = "ほん田　東十条"
          msg = "移転前の二郎系営業\n"
          msg += "しっかり豚出汁がきいており二郎に近い味。\n"
          msg += "様々な味のするとても優しいスープ。とにかくやさしい。本家よりはやはり少し軽めだが飲みやすくスープも美味しい。\n"
          msg += "豚は2種類とも柔らかい。味付きアブラは最高ね"
          ramen_url = "https://pbs.twimg.com/media/EVKZBRnUYAQr7Zc?format=jpg&name=large"
          ramen_url2 = "https://pbs.twimg.com/media/EVKZBT7U4AAjoMF?format=jpg&name=large"

        elif 20 <= num < 24: 
          shop_title = "八咫烏　九段下"
          msg = "八咫烏式asianな坦々麺＋ジャスミン追い飯＋ガパオ和え玉\n"
          msg += "汁なし坦々麺から始まり途中で2枚目のスープを投入し、汁あり坦々麺へ\n"
          msg += "和え玉もそのまま食べても汁に投入しても美味しい。最後に米も投入し、何度も楽しめ全てが美味しかった。\n"
          msg += "辛さ痺れもちょうどよかった"
          ramen_url = "https://pbs.twimg.com/media/EVKYVwiUcAA72cF?format=jpg&name=large"
          ramen_url2 = "https://pbs.twimg.com/media/EVKYVwdU8AEJFA7?format=jpg&name=large"
          ramen_url3 = "https://pbs.twimg.com/media/EVKYWGFUMAA88-k?format=jpg&name=large"
          ramen_url4 = "https://pbs.twimg.com/media/EVKYWHJUwAAt45K?format=jpg&name=large"

        elif 24 <= num < 28: 
          shop_title = "稲田堤　六等星"
          msg = "こってりラーメンDX(特製的な)\n"
          msg += "他には無いラーメン。\n"
          msg += "味はがっつり豚骨だがスープはどろっとしてる。見た目通り味は濃い目。\n"
          msg += "豚がホロホロでうまうま。\n"
          msg += "麺は太め"
          ramen_url = "https://pbs.twimg.com/media/EUm6h-jUcAE7pnL?format=jpg&name=large"

        elif 28 <= num < 32: 
          shop_title = "楽観　立川"
          msg = "特製琥珀(醤油)＋和え玉＋ミニチャーシューマヨ丼\n"
          msg += "あっさり系。うまいが量と値段が少し…\n"
          ramen_url = "https://pbs.twimg.com/media/EUm54zWU8AElwoR?format=jpg&name=large"
          ramen_url2 = "https://pbs.twimg.com/media/EUm55E6UwAAztg0?format=jpg&name=large"

        elif 32 <= num < 36: 
          shop_title = "吉村家　横浜"
          msg = "こってりラーメンDX(特製的な)\n"
          msg += "かなり久しぶりの吉村家\n"
          msg += "スープは濃く、チャーシューはスモークでうまかった。\n"
          msg += "海苔がデフォで多めでしっかり味のする少し分厚め？だったのが良き\n"
          ramen_url = "https://pbs.twimg.com/media/EUm5fgVU0AA8KSD?format=jpg&name=large"

        elif 36 <= num < 40: 
          shop_title = "ハイパーファットン　新羽"
          msg = "ラブリー汁なしアブラマシカラカラ＋豚増し\n"
          msg += "こちらの限定最終日\n"
          msg += "初訪問。味濃かったのでカラカラにしなくてよかったが、うまかった。\n"
          msg += "豚がつよつよ。\n"
          msg += "ラーメンフェス系で食べた時うまくて気になっていた店。\n"
          msg += "限定の種類も多いし通いたい"
          ramen_url = "https://pbs.twimg.com/media/EUm4147U8AAFWer?format=jpg&name=large"

        elif 40 <= num < 44: 
          shop_title = "ファミマ"
          msg = "ファミマの二郎っぽいやつ\n"
          msg += "セブンのがうまかったかな"
          ramen_url = "https://pbs.twimg.com/media/EUU2DCRUUAASKvT?format=jpg&name=large"

        elif 44 <= num < 48: 
          shop_title = "牛王　武蔵新城"
          msg = "濃厚こってりつけ麺\n"
          msg += "牛王ラーメン\n"
          msg += "どちらも牛出汁が強く出てた。\n"
          msg += "肉がうまかった。\n"
          msg += "牛王ラーメンはデミグラスソースのような味？で食べたことのない一杯"
          ramen_url = "https://pbs.twimg.com/media/EUU10WQU8AAwS82?format=jpg&name=large"
          ramen_url2 = "https://pbs.twimg.com/media/EUU10WNUUAY6GhF?format=jpg&name=large"

        elif 48 <= num < 52:
          shop_title = "柴崎亭　つつじヶ丘"
          msg = "玉ねぎ中華そば\n"
          msg += "限定250円の日\n"
          msg += "これが250円はアドみが深い\n"
          ramen_url = "https://pbs.twimg.com/media/EUCGcXGU8AAbTPY?format=jpg&name=large"

        elif 52 <= num < 56:
          shop_title = "柴崎亭　つつじヶ丘"
          msg = "飛騨牛と茄子のぶっ掛け(限定)\n"
          msg += "味の濃い味噌味の餡がうーまい。\n"
          msg += "飛騨牛と野菜たっぷり。\n"
          msg += "余った餡をライスにかけてもらえるサービス付き。\n"
          msg += "追い飯と聞いていたのにがっつり来て最高。\n"
          msg += "また食いたい"
          ramen_url = "https://pbs.twimg.com/media/ETyTAtlUEAUNsjp?format=jpg&name=large"
          ramen_url2 = "https://pbs.twimg.com/media/ETyTAtnUUAAzNVr?format=jpg&name=large"

        elif 56 <= num < 60:
          shop_title = "スープメン　ときわ台"
          msg = "鮭醤油らぁめん(確か)＋しらす丼\n"
          msg += "安定のうまさ。\n"
          msg += "キクラゲあまり好きじゃないんだけどシャキシャキでうまかった。\n"
          msg += "いつも完飲してしまう…"
          ramen_url = "https://pbs.twimg.com/media/ETyPPmgUUAAuVw1?format=jpg&name=large"
          ramen_url2 = "https://pbs.twimg.com/media/ETyPPmnUwAADpSp?format=jpg&name=large"

        elif 60 <= num < 64:
          shop_title = "セブンのとみたの豚ラーメン"
          msg = "改良された2回目のもの？\n"
          msg += "わりとうまいあ。\n"
          msg += "下手な店のよりうまいかもしれん。"
          ramen_url = "https://pbs.twimg.com/media/ETySKihU0AEq2Bf?format=jpg&name=large"

        elif 64 <= num < 68:
          shop_title = "黒須　神保町"
          msg = "トリュフ香る醤油ラーメン(限定)＋肉丼\n"
          msg += "トリュフが香り過ぎてて少し苦手だった。\n"
          msg += "肉丼はごま油強め。\n"
          msg += "今度は普通の食べたいかな。"
          ramen_url = "https://pbs.twimg.com/media/ETyR0iQU0AAKnR5?format=jpg&name=large"
          ramen_url2 = "https://pbs.twimg.com/media/ETyR0iUUYAEsiPt?format=jpg&name=large"

        elif 68 <= num < 72:
          shop_title = "覆麺智　神保町"
          msg = "牛テール塩ラーメン大盛(限定)\n"
          msg += "金曜昼限定だったもの。\n"
          msg += "思ってより牛出汁は弱めでかなりあっさりしたスープ"
          ramen_url = "https://pbs.twimg.com/media/ETyRpQuU4AAdZh1?format=jpg&name=large"

        elif 72 <= num < 76:
          shop_title = "らぁめん小池　上北沢"
          msg = "特製山椒らぁめん＋マヨチャー丼＋和え玉\n"
          msg += "醤油らぁめんに山椒を効かせたもの？\n"
          msg += "山椒が効いていて良かったがノーマルのがいいかも。"
          ramen_url = "https://pbs.twimg.com/media/ETyQMdQUcAcqWmV?format=jpg&name=large"
          ramen_url2 = "https://pbs.twimg.com/media/ETyQMdQVAAEw9hw?format=jpg&name=large"
          ramen_url3 = "https://pbs.twimg.com/media/ETyQMl9UcAAgTxI?format=jpg&name=large"

        elif 76 <= num < 80:
          shop_title = "府中二郎"
          msg = "大豚つけ麺ヤサイアブラカラメ\n"
          msg += "大豚でも普通に食えたが、後半疲れたので小豚でちょうどいいかな"
          ramen_url = "https://pbs.twimg.com/media/ETyP8pFUUAE6J3n?format=jpg&name=large"

        elif 80 <= num < 84:
          shop_title = "篠はら　要町"
          msg = "塩そば＋出汁炊きご飯\n"
          msg += "要の塩。月1塩そばDAYラストの塩そば。\n"
          msg += "肉出汁の効いたあっさり塩。\n"
          msg += "かなり飲みやすくおいしい。\n"
          msg += "ご飯はほんのり出汁\n"
          msg += "40.50並んでたなあ。回転は早いので1時間ほど。"
          ramen_url = "https://pbs.twimg.com/media/ETyPzivUcAErU-4?format=jpg&name=large"
          ramen_url2 = "https://pbs.twimg.com/media/ETyPziwUUAAFx6R?format=jpg&name=large"

        elif 84 <= num < 88:
          shop_title = "中華蕎麦きつね　芦花公園"
          msg = "特製中華蕎麦＋肉丼\n"
          msg += "あっさり醤油で美味しかったが、醤油味が少し薄めかな？あっさりだが液油は結構多め\n"
          msg += "思ったより量もあり\n"
          msg += "今度は濃厚を食べてみたい"
          ramen_url = "https://pbs.twimg.com/media/ETyPodkUYAE8cop?format=jpg&name=large"
          ramen_url2 = "https://pbs.twimg.com/media/ETyPodoU4AIOWnF?format=jpg&name=large"

        elif 88 <= num < 92:
          shop_title = "らぁめん小池　上北沢"
          msg = "特製醤油らぁめん\n"
          msg += "あっさり煮干しで飲みやすい。\n"
          msg += "トッピングも全て良い。マヨ多めのマヨチャー丼、そのまま食べて美味しい和え玉"
          ramen_url = "https://pbs.twimg.com/media/ETyPYp6UcAEC__X?format=jpg&name=large"
          ramen_url2 = "https://pbs.twimg.com/media/ETyPYp5U8AA_bKW?format=jpg&name=large"
          ramen_url3 = "https://pbs.twimg.com/media/ETyPYyIUUAAD1Vc?format=jpg&name=large"

        elif 92 <= num < 96:
          shop_title = "らぁめんやまぐち　高田馬場"
          msg = "スタミナまぜそば(限定)＋吊し焼き燻製チャーシュー＋大ライス\n"
          msg += "限定まぜそば\n"
          msg += "ジャンキーだが重すぎずうまい。追い飯もがっつり"
          ramen_url = "https://pbs.twimg.com/media/ETyO5lfUMAE5PN7?format=jpg&name=large"
          ramen_url2 = "https://pbs.twimg.com/media/ETyO6HrUMAMxD64?format=jpg&name=large"
          ramen_url3 = "https://pbs.twimg.com/media/ETyO5ljUwAAd988?format=jpg&name=large"

        else:
          shop_title = "つけめん　さなだ"
          msg = "夜鳴きそば(限定)＋トッピング色々＋生姜鷄ほぐし丼\n"
          msg += "生姜醤油的な\n"
          msg += "結構前のものなので曖昧で申し訳"
          ramen_url = "https://pbs.twimg.com/media/ETyOpUMVAAAEmF7?format=jpg&name=large"
          ramen_url2 = "https://pbs.twimg.com/media/ETyOpa2UwAA9qbC?format=jpg&name=large"
          ramen_url3 = "https://pbs.twimg.com/media/ETyOpUMUEAAITBG?format=jpg&name=large"

        embed = discord.Embed(title=shop_title,description=msg,color=discord.Colour.red())
        embed.set_image(url=ramen_url)

        if 'ramen_url2' in locals():
          await message.channel.send(embed=embed)
          embed = discord.Embed(color=discord.Colour.red())
          embed.set_image(url=ramen_url2)

        if 'ramen_url3' in locals():
          await message.channel.send(embed=embed)
          embed = discord.Embed(color=discord.Colour.red())
          embed.set_image(url=ramen_url3)

        if 'ramen_url4' in locals():
          await message.channel.send(embed=embed)
          embed = discord.Embed(color=discord.Colour.red())
          embed.set_image(url=ramen_url4)

        await message.channel.send(embed=embed)

client.run(deamon_apikey)
