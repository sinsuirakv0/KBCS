# 開発方針

- 変数名・関数名は英語、コメントは日本語。日本語を含むソース・文書はBOM付きUTF-8。
- 小さく再利用可能な実装と最小限のテストを優先する。
- 設計・実測・関数の関係は各領域のdocsへ残す。
- RustはGUI・DB・変換・制御、C++20は将来の戦闘・姿勢計算。描画と戦闘を分離する。
- 変更前に[設計](docs/architecture/README.md)、[データ契約](docs/data/README.md)、対象領域のdocsを読む。
- Webの解釈は暫定。仕様を推測せず、原本・版・出典を保持する。
- research資産を削除しない。大容量の解析生成物はresearch/.localへ保存する。
- 既存Ghidraプロジェクトを変更しない。GitHubへの書込・workflow実行は個別承認が必要。
- 不明な要件は大きな変更前に質問する。
- ネイティブ解析資料はresearch/README.mdの検索CLIを優先する。版・ABI・SHAを確認し、MCPの対象版と混同しない。大量の疑似コードを会話へ一括出力しない。
- 参照リポジトリは読み取り専用。実装進捗は[初期構築](docs/plans/initial-foundation.md)。
