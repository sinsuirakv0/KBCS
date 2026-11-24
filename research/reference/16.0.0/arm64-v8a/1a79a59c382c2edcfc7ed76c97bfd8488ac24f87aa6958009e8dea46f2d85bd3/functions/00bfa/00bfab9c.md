# 00bfab9c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7e154`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e154.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0020.md#compare-0fd1040abb191528adcccd5ea57b04cf)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfafc4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfafc4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-2cf1ea63282e78eed9f59259431767ed)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfab9c",
  "name": "_ZNSt6__ndk18ios_base7failureD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dfdf5589674f079308e6f234ab2e4b0511fdbe200b44032b9f88c3e7cb49d9ff",
  "source_text_sha256": "dfdf5589674f079308e6f234ab2e4b0511fdbe200b44032b9f88c3e7cb49d9ff",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfab9c",
        "00bfabc7"
      ]
    ],
    "bytes_sha256": "700adb582b1397c2fb077dd743342302da19befa70dfb474934a3fbed46142c3",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c5dec0](../00c5d/00c5dec0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 129 bytes

~~~c

void _ZNSt6__ndk18ios_base7failureD0Ev(void *param_1)

{
  _ZNSt6__ndk18ios_base7failureD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfab9c"></a> `00bfab9c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfaba0"></a> `00bfaba0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfaba4"></a> `00bfaba4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfaba8"></a> `00bfaba8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfabac"></a> `00bfabac` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfabb0"></a> `00bfabb0` | `c4 8c 01 94` | bl 0x00c5dec0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfabb4"></a> `00bfabb4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfabb8"></a> `00bfabb8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfabbc"></a> `00bfabbc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfabc0"></a> `00bfabc0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfabc4"></a> `00bfabc4` | `bb 73 01 14` | b 0x00c57ab0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfab9c`](#insn-00bfab9c) 範囲 `[['00bfab9c', '00bfabc7']]`

## 命令位置別の参照

- [`00bfaba0`](#insn-00bfaba0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaba4`](#insn-00bfaba4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfabb0`](#insn-00bfabb0) → [`00c5dec0`](../00c5d/00c5dec0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dec0` · 推定シンボル `None` · 推定型 `None`
- [`00bfabb8`](#insn-00bfabb8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfabbc`](#insn-00bfabbc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfabc4`](#insn-00bfabc4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfaba0`](#insn-00bfaba0)

~~~json
{
  "source": "00bfaba0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaba4`](#insn-00bfaba4)

~~~json
{
  "source": "00bfaba4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfabb0`](#insn-00bfabb0)

~~~json
{
  "source": "00bfabb0",
  "target": "00c5dec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfabb8`](#insn-00bfabb8)

~~~json
{
  "source": "00bfabb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfabbc`](#insn-00bfabbc)

~~~json
{
  "source": "00bfabbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfabc4`](#insn-00bfabc4)

~~~json
{
  "source": "00bfabc4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
