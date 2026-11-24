# 00bcbd8c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5c88c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c88c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0017.md#compare-1fc25db11bfbf107df383ba0ee210d6f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcc1b4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc1b4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-580f8f899a512b1f9e7ad742af5480ef)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbd8c",
  "name": "_ZN8firebase4auth23GetCredentialFutureImplEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f6e41839343f179f054c0e19b9c431dbd681312db7328e30499d1392491581eb",
  "source_text_sha256": "f6e41839343f179f054c0e19b9c431dbd681312db7328e30499d1392491581eb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbd8c",
        "00bcbd9b"
      ]
    ],
    "bytes_sha256": "806041d4e0e124390d0bd1455a719a4fb04f649ee9367f80f1216fc65434f0d5",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d750](../00c5d/00c5d750.md)

## 呼び出し先

- [00c5b930](../00c5b/00c5b930.md)

## 関連文字列（未確認候補）

~~~text
"Auth-Credentials"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 255 bytes

~~~c

void _ZN8firebase4auth23GetCredentialFutureImplEv(void)

{
                    /* try { // try from 00bcbd90 to 00ccbd9b has its CatchHandler @ 00bcbdf4 */
  _ZN8firebase16StaticFutureData22GetFutureDataForModuleEPKvi("Auth-Credentials",1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbd8c"></a> `00bcbd8c` | `20 ba ff 90` | adrp x0,0x30f000 | `FALL_THROUGH`
<a id="insn-00bcbd90"></a> `00bcbd90` | `00 8c 00 91` | add x0,x0,#0x23 | `FALL_THROUGH`
<a id="insn-00bcbd94"></a> `00bcbd94` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbd98"></a> `00bcbd98` | `e6 3e 02 14` | b 0x00c5b930 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbd8c`](#insn-00bcbd8c) 範囲 `[['00bcbd8c', '00bcbd8f']]`
  - `FALL_THROUGH` [`00bcbd8c`](#insn-00bcbd8c) → [`00bcbd90`](#insn-00bcbd90)
- ブロック [`00bcbd90`](#insn-00bcbd90) 範囲 `[['00bcbd90', '00bcbd9b']]`

## 命令位置別の参照

- [`00bcbd90`](#insn-00bcbd90) → `0030f023`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcbd98`](#insn-00bcbd98) → [`00c5b930`](../00c5b/00c5b930.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b930` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbd90`](#insn-00bcbd90)

~~~json
{
  "source": "00bcbd90",
  "target": "0030f023",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030f023",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "417574682d43726564656e7469616c7300",
  "capture_start": "0030f023",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcbd98`](#insn-00bcbd98)

~~~json
{
  "source": "00bcbd98",
  "target": "00c5b930",
  "target_space": "ram",
  "resolution": "function"
}
~~~
