mmd_tools
===========
mmd_toolsはblender用MMD(MikuMikuDance)モデルデータ(.pmx)およびモーションデータ(.vmd)インポータです。

環境
----
### 対応バージョン
blender 2.67以降

### 動作確認環境
Windows 7 + blender 2.67 64bit

使用方法
---------
### ダウンロード

* mmd_toolsはGitHubで公開しています。
    * https://github.com/sugiany/blender_mmd_tools
* 安定版は下記リンクから最新版をダウンロードしてください。
    * [Tags](https://github.com/sugiany/blender_mmd_tools/tags)
* 開発版はmasterブランチのHEADを取得してください。
    * [master.zip](https://github.com/sugiany/blender_mmd_tools/archive/master.zip)

### インストール
展開したアーカイブ内のmmd_toolsディレクトリをaddonディレクトリにコピーしてください。

    .../blender-2.67-windows64/2.67/scripts/addons/

### Addonのロード
1. User PrefernceのAddonsから"Object: mmd_tools"探してチェックを入れてください。
   (検索ボックスにmmdと入力すると簡単に探せます。)
2. 3D View左のパネルにMMD Toolsのパネルが表示されます。

### MMDモデルデータ読み込み
1. mmd_toolsパネルの"import/Model"ボタンを選択してください。
2. ファイル選択画面でpmxファイルを選択すると、選択されたモデルをインポートします。

### モーションデータの読み込み
1. あらかじめ読み込んでおいたモデルのMeshとArmature、Cameraを選択してください。(選択していない項目はインポートされません)
2. mmd_toolsパネルの"import/Motion"ボタンを選択してください。
3. ファイル選択画面でvmdファイルを選択すると選択中のオブジェクトへモーションをインポートします。
4. 「update scene settings」チェックボックスをオンにしておくと、モーションの読み込み後にフレームレンジ等のシーン設定を自動更新します。

各種機能詳細
-------------------------------
### Import pmx
pmxファイルをインポートします。
各オプションはデフォルト推薦です。
剛体情報を読み込みたくない場合は、"import only non dynamics rigid bodies"オプションをオンにしてください。

* scale
    * スケールです。Import vmd時のスケールと統一してください。
* rename bones
    * ボーンの名前をblenderに適した名前にリネームします。（右腕→腕.Lなど）
* delete tip bones
    * 試験的な機能です。通常、使用する必要はありません。
* hide rigid bodies and joints
    *  剛体情報を持つ各種オブジェクトを非表示にします。
* import only non dynamics rigid bodies
    * ボーン追従の剛体のみインポートします。clothやsoft bodyを使用する等、剛体情報が不要な場合に使用してください。
* ignore non collision groups
    * 非衝突グループを読み込みません。モデルの読み込み時にフリーズしてしまう場合に使用してください。
* distance of ignore collisions
    * 非衝突グループの解決範囲を指定します。指定された距離より離れている剛体同士は非衝突グループの設定を適用しません。

### Import vmd
現在選択中のArmature、MeshおよびCameraにvmdファイルのモーションを適用します。

* scale
    * スケールです。Import pmx時のスケールと統一してください。
* margin
    * 物理シミュレーション用の余白フレームです。
    * モーションの初期位置が原点から大きく離れている場合、モーション開始時にモデルが瞬間移動してしまうため物理シミュレーションが破綻します。
    この現象を回避するため、blenderのタイムライン開始とモーション開始の間に余白を挿入します。
    * モーション開始時に剛体を安定させる効果もあります。
* update scene settings
    * モーションデータ読み込み後にフレームレンジおよびフレームレートの自動設定を行います。
    * フレームレンジは現在シーン中に存在するアニメーションを全て再生するために必要なレンジを設定します。
    * フレームレートを30fpsに変更します。

### Set frame range
フレームレンジは現在シーン中に存在するアニメーションを全て再生するために必要なレンジを設定します。
また、フレームレートを30fpsに変更します。
* Import vmdのupdate scene settingsオプションと同じ機能です。

### View

#### GLSL
GLSLモードで表示するための必要設定を自動で行います。
* ShadingをGLSLに切り替えます。
* Shadelessチェックボックスがオンの場合、現在のシーン内全てのマテリアルをshadelessにします。
* shadelessチェックボックスがオフの場合、Hemiライトを追加します。
* ボタンを押したareaの3DViewのシェーディングをTEXUTEDに変更します。

#### Reset
GLSLボタンで変更した内容を初期状態に戻します。


#### Separate by materials
選択したメッシュオブジェクトのメッシュをマテリアル毎に分割し、分割後のオブジェクト名を各マテリアル名に変更します。
* blenderデフォルトの"Separate"→"By Material"機能を使用しています。

#### To cycles
選択したメッシュオブジェクトのblenderRender用マテリアルをcycles用に変換します。
* 何の根拠もない適当な変換です。
* 完了メッセージなどは表示されません。マテリアルパネルから変換されているかどうか確認してください。


その他
------
* カメラとキャラクタモーションが別ファイルの場合は、ArmatureとMeshを選択してキャラモーション、Cameraを選択してカメラモーションというように2回に分けてインポートしてください。
* モーションデータのアサインは"mmd_tools"でインポートしたモデルのみ可能です。
* カメラはMMD_Cameraという名前のEmptyオブジェクトを生成し、このオブジェクトにモーションをアサインします。
* 複数のモーションをインポートする場合やフレームにオフセットをつけてインポートしたい場合は、NLAエディタでアニメーションを編集してください。
* アニメーションの初期位置がモデルの原点と大きく離れている場合、剛体シミュレーションが破綻することgあります。その際は、vmdインポートパラメータ"margin"を大きくしてください。
* pmdのインポートには対応していません。pmdモデルを読み込みたい場合は、PMDEditorでpmx形式に変換してからインポートしてください。(将来的には対応したいです。)
* pmxインポートについて
    * 頂点のウェイト情報がSDEFの場合、BDEF2と同じ扱いを行います。
    * 頂点モーフ以外のモーフ情報には対応していません。
    * 剛体設定の"物理+ボーン位置合わせ"は"物理演算"として扱います。
* 複数のpmxファイルをインポートする場合はscaleを統一してください。

既知の問題
----------
* 剛体の非衝突グループを強引に解決しているため、剛体の数が多いモデルを読み込むとフリーズすることがあります。
    * 正確には完全なフリーズではなく、読み込みに異常な時間がかかっているだけです。
    * フリーズするモデルを読み込む場合は、"ignore non collision groups"オプションにチェックを入れてください。
    * 上記オプションをオンにした場合、意図しない剛体同士が干渉し、正常に物理シミュレーションが動作しない可能性があります。

バグ・要望・質問等
------------------
GitHubのIssueに登録するか、twitterでどうぞ。  
[@sugiany](https://twitter.com/sugiany)

変更履歴
--------
CHANGELOG.mdを参照してください。

ライセンス
----------
Copyright &copy; 2012-2013 sugiany  
Distributed under the MIT License.  
