# 00bbcee0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0174.md#review-c27574d01304dc947549adfee5afed6c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbd308`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd308.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0079.md#compare-14a0546615a65f18e70cb72410be638a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbcee0",
  "name": "FUN_00bbcee0",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bac9ffd4c7ac5959aa460cf182b19bc8dcf07e200894612c67c9cde30c53b9c2",
  "source_text_sha256": "bac9ffd4c7ac5959aa460cf182b19bc8dcf07e200894612c67c9cde30c53b9c2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbcee0",
        "00bbcf2b"
      ]
    ],
    "bytes_sha256": "4c4ae6c4bd94977b05d29220e04f087a2bf5bfac8a336ae8ff38f1e97f5e45fa",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bbcd98](../00bbc/00bbcd98.md)
- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5cfc0](../00c5c/00c5cfc0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 335 bytes

~~~c

void FUN_00bbcee0(undefined8 param_1)

{
  long lVar1;
  
  lVar1 = DAT_01125f70;
  if (DAT_01125f70 != 0) {
    _ZN8firebase5Mutex7AcquireEv(DAT_01125f70);
    DAT_01126008 = 1;
    FUN_00bbcd98();
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
  }
  _ZN8firebase9messaging36NotifyListenerOnRegistrationReceivedEPKc(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbcee0"></a> `00bbcee0` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbcee4"></a> `00bbcee4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcee8"></a> `00bbcee8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbceec"></a> `00bbceec` | `48 2b 00 b0` | adrp x8,0x1125000 | `FALL_THROUGH`
<a id="insn-00bbcef0"></a> `00bbcef0` | `14 b9 47 f9` | ldr x20,[x8, #0xf70] | `FALL_THROUGH`
<a id="insn-00bbcef4"></a> `00bbcef4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbcef8"></a> `00bbcef8` | `34 01 00 b4` | cbz x20,0x00bbcf1c | `CONDITIONAL_JUMP`
<a id="insn-00bbcefc"></a> `00bbcefc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbcf00"></a> `00bbcf00` | `c0 75 02 94` | bl 0x00c5a600 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcf04"></a> `00bbcf04` | `48 2b 00 d0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbcf08"></a> `00bbcf08` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcf0c"></a> `00bbcf0c` | `09 21 00 39` | strb w9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbcf10"></a> `00bbcf10` | `a2 ff ff 97` | bl 0x00bbcd98 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcf14"></a> `00bbcf14` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbcf18"></a> `00bbcf18` | `be 75 02 94` | bl 0x00c5a610 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcf1c"></a> `00bbcf1c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcf20"></a> `00bbcf20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbcf24"></a> `00bbcf24` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbcf28"></a> `00bbcf28` | `26 80 02 14` | b 0x00c5cfc0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbcee0`](#insn-00bbcee0) 範囲 `[['00bbcee0', '00bbcefb']]`
  - `CONDITIONAL_JUMP` [`00bbcef8`](#insn-00bbcef8) → [`00bbcf1c`](#insn-00bbcf1c)
  - `FALL_THROUGH` [`00bbcef8`](#insn-00bbcef8) → [`00bbcefc`](#insn-00bbcefc)
- ブロック [`00bbcefc`](#insn-00bbcefc) 範囲 `[['00bbcefc', '00bbcf1b']]`
  - `FALL_THROUGH` [`00bbcf18`](#insn-00bbcf18) → [`00bbcf1c`](#insn-00bbcf1c)
- ブロック [`00bbcf1c`](#insn-00bbcf1c) 範囲 `[['00bbcf1c', '00bbcf2b']]`

## 命令位置別の参照

- [`00bbcee0`](#insn-00bbcee0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcee4`](#insn-00bbcee4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcef0`](#insn-00bbcef0) → `01125f70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbcef8`](#insn-00bbcef8) → [`00bbcf1c`](#insn-00bbcf1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf00`](#insn-00bbcf00) → [`00c5a600`](../00c5a/00c5a600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a600` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf0c`](#insn-00bbcf0c) → `01126008`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbcf10`](#insn-00bbcf10) → [`00bbcd98`](00bbcd98.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbcd98` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf18`](#insn-00bbcf18) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf1c`](#insn-00bbcf1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf28`](#insn-00bbcf28) → [`00c5cfc0`](../00c5c/00c5cfc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cfc0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbcee0`](#insn-00bbcee0)

~~~json
{
  "source": "00bbcee0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcee4`](#insn-00bbcee4)

~~~json
{
  "source": "00bbcee4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcef0`](#insn-00bbcef0)

~~~json
{
  "source": "00bbcef0",
  "target": "01125f70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125f70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbcef8`](#insn-00bbcef8)

~~~json
{
  "source": "00bbcef8",
  "target": "00bbcf1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcf00`](#insn-00bbcf00)

~~~json
{
  "source": "00bbcf00",
  "target": "00c5a600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcf0c`](#insn-00bbcf0c)

~~~json
{
  "source": "00bbcf0c",
  "target": "01126008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126008",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbcf10`](#insn-00bbcf10)

~~~json
{
  "source": "00bbcf10",
  "target": "00bbcd98",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcf18`](#insn-00bbcf18)

~~~json
{
  "source": "00bbcf18",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcf1c`](#insn-00bbcf1c)

~~~json
{
  "source": "00bbcf1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcf28`](#insn-00bbcf28)

~~~json
{
  "source": "00bbcf28",
  "target": "00c5cfc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
