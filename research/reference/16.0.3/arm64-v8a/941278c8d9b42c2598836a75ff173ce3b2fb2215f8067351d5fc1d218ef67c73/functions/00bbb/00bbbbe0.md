# 00bbbbe0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbabec`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbabec.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-9c22a72484e44f97abcc0ce7753fc957)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbbe0",
  "name": "FUN_00bbbbe0",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d216a75d614d10ff5756f9bffc7d281d25bf84bf53889d1805c40d7a035b8369",
  "source_text_sha256": "d216a75d614d10ff5756f9bffc7d281d25bf84bf53889d1805c40d7a035b8369",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbbbe0",
        "00bbbc9b"
      ]
    ],
    "bytes_sha256": "b720ddf240696b6dc16b4ad54c4152510a8e8eaef15b9a25aa6433e97ef5fbed",
    "instruction_count": 47,
    "instruction_bytes": 188,
    "body_bytes": 188,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

- [00bbb6b8](../00bbb/00bbb6b8.md)
- [00bbc0e8](../00bbc/00bbc0e8.md)

## 呼び出し先

- [00c5c000](../00c5c/00c5c000.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 638 bytes

~~~c

void FUN_00bbbbe0(long *param_1)

{
  if (DAT_01127368 != 0) {
    if (DAT_01127370 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01127370 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01127368);
    DAT_01127368 = 0;
  }
  if (DAT_011273d8 != 0) {
    if (DAT_011273e0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011273e0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011273d8);
    DAT_011273d8 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbbbe0"></a> `00bbbbe0` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bbbbe4"></a> `00bbbbe4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbbe8"></a> `00bbbbe8` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbbec"></a> `00bbbbec` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbbbf0"></a> `00bbbbf0` | `74 2b 00 90` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbbbf4"></a> `00bbbbf4` | `81 b6 41 f9` | ldr x1,[x20, #0x368] | `FALL_THROUGH`
<a id="insn-00bbbbf8"></a> `00bbbbf8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbbbfc"></a> `00bbbbfc` | `21 02 00 b4` | cbz x1,0x00bbbc40 | `CONDITIONAL_JUMP`
<a id="insn-00bbbc00"></a> `00bbbc00` | `75 2b 00 90` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbbc04"></a> `00bbbc04` | `a8 c2 4d 39` | ldrb w8,[x21, #0x370] | `FALL_THROUGH`
<a id="insn-00bbbc08"></a> `00bbbc08` | `c8 00 00 34` | cbz w8,0x00bbbc20 | `CONDITIONAL_JUMP`
<a id="insn-00bbbc0c"></a> `00bbbc0c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbbc10"></a> `00bbbc10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbc14"></a> `00bbbc14` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bbbc18"></a> `00bbbc18` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbbc1c"></a> `00bbbc1c` | `bf c2 0d 39` | strb wzr,[x21, #0x370] | `FALL_THROUGH`
<a id="insn-00bbbc20"></a> `00bbbc20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbc24"></a> `00bbbc24` | `f7 80 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbc28"></a> `00bbbc28` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbbc2c"></a> `00bbbc2c` | `81 b6 41 f9` | ldr x1,[x20, #0x368] | `FALL_THROUGH`
<a id="insn-00bbbc30"></a> `00bbbc30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbc34"></a> `00bbbc34` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bbbc38"></a> `00bbbc38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbbc3c"></a> `00bbbc3c` | `9f b6 01 f9` | str xzr,[x20, #0x368] | `FALL_THROUGH`
<a id="insn-00bbbc40"></a> `00bbbc40` | `74 2b 00 90` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbbc44"></a> `00bbbc44` | `81 ee 41 f9` | ldr x1,[x20, #0x3d8] | `FALL_THROUGH`
<a id="insn-00bbbc48"></a> `00bbbc48` | `21 02 00 b4` | cbz x1,0x00bbbc8c | `CONDITIONAL_JUMP`
<a id="insn-00bbbc4c"></a> `00bbbc4c` | `75 2b 00 90` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbbc50"></a> `00bbbc50` | `a8 82 4f 39` | ldrb w8,[x21, #0x3e0] | `FALL_THROUGH`
<a id="insn-00bbbc54"></a> `00bbbc54` | `c8 00 00 34` | cbz w8,0x00bbbc6c | `CONDITIONAL_JUMP`
<a id="insn-00bbbc58"></a> `00bbbc58` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbbc5c"></a> `00bbbc5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbc60"></a> `00bbbc60` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bbbc64"></a> `00bbbc64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbbc68"></a> `00bbbc68` | `bf 82 0f 39` | strb wzr,[x21, #0x3e0] | `FALL_THROUGH`
<a id="insn-00bbbc6c"></a> `00bbbc6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbc70"></a> `00bbbc70` | `e4 80 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbc74"></a> `00bbbc74` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbbc78"></a> `00bbbc78` | `81 ee 41 f9` | ldr x1,[x20, #0x3d8] | `FALL_THROUGH`
<a id="insn-00bbbc7c"></a> `00bbbc7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbc80"></a> `00bbbc80` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bbbc84"></a> `00bbbc84` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbbc88"></a> `00bbbc88` | `9f ee 01 f9` | str xzr,[x20, #0x3d8] | `FALL_THROUGH`
<a id="insn-00bbbc8c"></a> `00bbbc8c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbc90"></a> `00bbbc90` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbc94"></a> `00bbbc94` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bbbc98"></a> `00bbbc98` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbbbe0`](#insn-00bbbbe0) 範囲 `[['00bbbbe0', '00bbbbff']]`
  - `CONDITIONAL_JUMP` [`00bbbbfc`](#insn-00bbbbfc) → [`00bbbc40`](#insn-00bbbc40)
  - `FALL_THROUGH` [`00bbbbfc`](#insn-00bbbbfc) → [`00bbbc00`](#insn-00bbbc00)
- ブロック [`00bbbc00`](#insn-00bbbc00) 範囲 `[['00bbbc00', '00bbbc0b']]`
  - `CONDITIONAL_JUMP` [`00bbbc08`](#insn-00bbbc08) → [`00bbbc20`](#insn-00bbbc20)
  - `FALL_THROUGH` [`00bbbc08`](#insn-00bbbc08) → [`00bbbc0c`](#insn-00bbbc0c)
- ブロック [`00bbbc0c`](#insn-00bbbc0c) 範囲 `[['00bbbc0c', '00bbbc1f']]`
  - `FALL_THROUGH` [`00bbbc1c`](#insn-00bbbc1c) → [`00bbbc20`](#insn-00bbbc20)
- ブロック [`00bbbc20`](#insn-00bbbc20) 範囲 `[['00bbbc20', '00bbbc3f']]`
  - `FALL_THROUGH` [`00bbbc3c`](#insn-00bbbc3c) → [`00bbbc40`](#insn-00bbbc40)
- ブロック [`00bbbc40`](#insn-00bbbc40) 範囲 `[['00bbbc40', '00bbbc4b']]`
  - `CONDITIONAL_JUMP` [`00bbbc48`](#insn-00bbbc48) → [`00bbbc8c`](#insn-00bbbc8c)
  - `FALL_THROUGH` [`00bbbc48`](#insn-00bbbc48) → [`00bbbc4c`](#insn-00bbbc4c)
- ブロック [`00bbbc4c`](#insn-00bbbc4c) 範囲 `[['00bbbc4c', '00bbbc57']]`
  - `CONDITIONAL_JUMP` [`00bbbc54`](#insn-00bbbc54) → [`00bbbc6c`](#insn-00bbbc6c)
  - `FALL_THROUGH` [`00bbbc54`](#insn-00bbbc54) → [`00bbbc58`](#insn-00bbbc58)
- ブロック [`00bbbc58`](#insn-00bbbc58) 範囲 `[['00bbbc58', '00bbbc6b']]`
  - `FALL_THROUGH` [`00bbbc68`](#insn-00bbbc68) → [`00bbbc6c`](#insn-00bbbc6c)
- ブロック [`00bbbc6c`](#insn-00bbbc6c) 範囲 `[['00bbbc6c', '00bbbc8b']]`
  - `FALL_THROUGH` [`00bbbc88`](#insn-00bbbc88) → [`00bbbc8c`](#insn-00bbbc8c)
- ブロック [`00bbbc8c`](#insn-00bbbc8c) 範囲 `[['00bbbc8c', '00bbbc9b']]`

## 命令位置別の参照

- [`00bbbbe0`](#insn-00bbbbe0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbe4`](#insn-00bbbbe4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbe8`](#insn-00bbbbe8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbf4`](#insn-00bbbbf4) → `01127368`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbbfc`](#insn-00bbbbfc) → [`00bbbc40`](#insn-00bbbc40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc04`](#insn-00bbbc04) → `01127370`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbbc08`](#insn-00bbbc08) → [`00bbbc20`](#insn-00bbbc20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc1c`](#insn-00bbbc1c) → `01127370`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbbc24`](#insn-00bbbc24) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc2c`](#insn-00bbbc2c) → `01127368`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbc3c`](#insn-00bbbc3c) → `01127368`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbc44`](#insn-00bbbc44) → `011273d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbc48`](#insn-00bbbc48) → [`00bbbc8c`](#insn-00bbbc8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc50`](#insn-00bbbc50) → `011273e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbbc54`](#insn-00bbbc54) → [`00bbbc6c`](#insn-00bbbc6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc68`](#insn-00bbbc68) → `011273e0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbbc70`](#insn-00bbbc70) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc78`](#insn-00bbbc78) → `011273d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbc88`](#insn-00bbbc88) → `011273d8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbc8c`](#insn-00bbbc8c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc90`](#insn-00bbbc90) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbbbe0`](#insn-00bbbbe0)

~~~json
{
  "source": "00bbbbe0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbbe4`](#insn-00bbbbe4)

~~~json
{
  "source": "00bbbbe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbbe8`](#insn-00bbbbe8)

~~~json
{
  "source": "00bbbbe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbbf4`](#insn-00bbbbf4)

~~~json
{
  "source": "00bbbbf4",
  "target": "01127368",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127368",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbbfc`](#insn-00bbbbfc)

~~~json
{
  "source": "00bbbbfc",
  "target": "00bbbc40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc04`](#insn-00bbbc04)

~~~json
{
  "source": "00bbbc04",
  "target": "01127370",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127370",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbc08`](#insn-00bbbc08)

~~~json
{
  "source": "00bbbc08",
  "target": "00bbbc20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc1c`](#insn-00bbbc1c)

~~~json
{
  "source": "00bbbc1c",
  "target": "01127370",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127370",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbc24`](#insn-00bbbc24)

~~~json
{
  "source": "00bbbc24",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbc2c`](#insn-00bbbc2c)

~~~json
{
  "source": "00bbbc2c",
  "target": "01127368",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127368",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbc3c`](#insn-00bbbc3c)

~~~json
{
  "source": "00bbbc3c",
  "target": "01127368",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127368",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbc44`](#insn-00bbbc44)

~~~json
{
  "source": "00bbbc44",
  "target": "011273d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011273d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbc48`](#insn-00bbbc48)

~~~json
{
  "source": "00bbbc48",
  "target": "00bbbc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc50`](#insn-00bbbc50)

~~~json
{
  "source": "00bbbc50",
  "target": "011273e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011273e0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbc54`](#insn-00bbbc54)

~~~json
{
  "source": "00bbbc54",
  "target": "00bbbc6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc68`](#insn-00bbbc68)

~~~json
{
  "source": "00bbbc68",
  "target": "011273e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011273e0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbc70`](#insn-00bbbc70)

~~~json
{
  "source": "00bbbc70",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbc78`](#insn-00bbbc78)

~~~json
{
  "source": "00bbbc78",
  "target": "011273d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011273d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbc88`](#insn-00bbbc88)

~~~json
{
  "source": "00bbbc88",
  "target": "011273d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011273d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbc8c`](#insn-00bbbc8c)

~~~json
{
  "source": "00bbbc8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc90`](#insn-00bbbc90)

~~~json
{
  "source": "00bbbc90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
