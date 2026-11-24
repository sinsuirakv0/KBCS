# 006dafdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `006b1220`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1220.md) · 移動量 `+0x29dbc`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0014.md#compare-fb1e3c1cc3d05193270a42974583fd30)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `006db01c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006db01c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0021.md#compare-f0e4d40243b1a5894cc24bbbce7c663c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006dafdc",
  "name": "FUN_006dafdc",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "01727eb86aa498afba91932f53d48032b909896b0ad395ae6d5328cbc0caf44a",
  "source_text_sha256": "01727eb86aa498afba91932f53d48032b909896b0ad395ae6d5328cbc0caf44a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006dafdc",
        "006db02b"
      ]
    ],
    "bytes_sha256": "a5c11a458ebef76a1c96f53175bdfb42d0ed64058ecd5e69a01caf27f56ad886",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a2b0f0](../00a2b/00a2b0f0.md)

## 呼び出し先

- [00480af8](../00480/00480af8.md)
- [00480b50](../00480/00480b50.md)
- [00480d08](../00480/00480d08.md)
- [00481058](../00481/00481058.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 255 bytes

~~~c

void FUN_006dafdc(undefined4 *param_1,undefined8 param_2)

{
  FUN_00480b50(param_2,*param_1);
  FUN_00481058(*(undefined8 *)(param_1 + 2),param_2);
  FUN_00480af8(param_2,param_1[4]);
  FUN_00480d08(param_2,*(undefined1 *)(param_1 + 0xe));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006dafdc"></a> `006dafdc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-006dafe0"></a> `006dafe0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006dafe4"></a> `006dafe4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-006dafe8"></a> `006dafe8` | `08 00 40 b9` | ldr w8,[x0] | `FALL_THROUGH`
<a id="insn-006dafec"></a> `006dafec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-006daff0"></a> `006daff0` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-006daff4"></a> `006daff4` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-006daff8"></a> `006daff8` | `e1 03 08 2a` | mov w1,w8 | `FALL_THROUGH`
<a id="insn-006daffc"></a> `006daffc` | `d5 96 f6 97` | bl 0x00480b50 | `UNCONDITIONAL_CALL`
<a id="insn-006db000"></a> `006db000` | `60 06 40 fd` | ldr d0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-006db004"></a> `006db004` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006db008"></a> `006db008` | `14 98 f6 97` | bl 0x00481058 | `UNCONDITIONAL_CALL`
<a id="insn-006db00c"></a> `006db00c` | `61 12 40 b9` | ldr w1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-006db010"></a> `006db010` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006db014"></a> `006db014` | `b9 96 f6 97` | bl 0x00480af8 | `UNCONDITIONAL_CALL`
<a id="insn-006db018"></a> `006db018` | `61 e2 40 39` | ldrb w1,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-006db01c"></a> `006db01c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006db020"></a> `006db020` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006db024"></a> `006db024` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-006db028"></a> `006db028` | `38 97 f6 17` | b 0x00480d08 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006dafdc`](#insn-006dafdc) 範囲 `[['006dafdc', '006db02b']]`

## 命令位置別の参照

- [`006dafdc`](#insn-006dafdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dafe0`](#insn-006dafe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daffc`](#insn-006daffc) → [`00480b50`](../00480/00480b50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480b50` · 推定シンボル `None` · 推定型 `None`
- [`006db008`](#insn-006db008) → [`00481058`](../00481/00481058.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00481058` · 推定シンボル `None` · 推定型 `None`
- [`006db014`](#insn-006db014) → [`00480af8`](../00480/00480af8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480af8` · 推定シンボル `None` · 推定型 `None`
- [`006db020`](#insn-006db020) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006db024`](#insn-006db024) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006db028`](#insn-006db028) → [`00480d08`](../00480/00480d08.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480d08` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006dafdc`](#insn-006dafdc)

~~~json
{
  "source": "006dafdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dafe0`](#insn-006dafe0)

~~~json
{
  "source": "006dafe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daffc`](#insn-006daffc)

~~~json
{
  "source": "006daffc",
  "target": "00480b50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006db008`](#insn-006db008)

~~~json
{
  "source": "006db008",
  "target": "00481058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006db014`](#insn-006db014)

~~~json
{
  "source": "006db014",
  "target": "00480af8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006db020`](#insn-006db020)

~~~json
{
  "source": "006db020",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006db024`](#insn-006db024)

~~~json
{
  "source": "006db024",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006db028`](#insn-006db028)

~~~json
{
  "source": "006db028",
  "target": "00480d08",
  "target_space": "ram",
  "resolution": "function"
}
~~~
