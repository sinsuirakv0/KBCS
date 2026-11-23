# 00bdae3c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdad7c`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdad7c.md) · 移動量 `+0xc0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0045.md#compare-521b96dd89b3eef39588a074f6906a2c)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdae7c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdae7c.md) · 移動量 `+0x40`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/machine_only_observed-0044.md#compare-cf6892722ed23093bfcf396da705e7e3)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdae3c",
  "name": "FUN_00bdae3c",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "944855150ae5497b9dd5a2bc8c67f451d04a8d40d28f3689a49d1b75cb081751",
  "source_text_sha256": "944855150ae5497b9dd5a2bc8c67f451d04a8d40d28f3689a49d1b75cb081751",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdae3c",
        "00bdae43"
      ]
    ],
    "bytes_sha256": "f01374a33c08e4af485034b3e5d2a14511ae92ca2bcb778241dd7f20b63d46f0",
    "instruction_count": 2,
    "instruction_bytes": 8,
    "body_bytes": 8,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [008d40c0](../008d4/008d40c0.md)

## 呼び出し先

- [008d5008](../008d5/008d5008.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 133 bytes

~~~c

void FUN_00bdae3c(undefined1 param_1 [16])

{
  long in_x9;
  
  FUN_008d5008(param_1,*(undefined8 *)(in_x9 + 0xe10));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdae3c"></a> `00bdae3c` | `21 85 c3 3d` | ldr q1,[x9, #0xe10] | `FALL_THROUGH`
<a id="insn-00bdae40"></a> `00bdae40` | `72 e8 f3 17` | b 0x008d5008 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdae3c`](#insn-00bdae3c) 範囲 `[['00bdae3c', '00bdae43']]`

## 命令位置別の参照

- [`00bdae40`](#insn-00bdae40) → [`008d5008`](../008d5/008d5008.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008d5008` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdae40`](#insn-00bdae40)

~~~json
{
  "source": "00bdae40",
  "target": "008d5008",
  "target_space": "ram",
  "resolution": "function"
}
~~~
