# 00bba7bc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bb97c8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb97c8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-7a03a1618c65f874e029e72d6ef00f10)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bba7bc",
  "name": "_ZN8firebase9messaging17NotifyListenerSetEPNS0_8ListenerE",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b1268573302aa97b31519529f640bfd602ae5786282f20d538ac27912d28e028",
  "source_text_sha256": "b1268573302aa97b31519529f640bfd602ae5786282f20d538ac27912d28e028",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bba7bc",
        "00bba85f"
      ]
    ],
    "bytes_sha256": "e213f09eecb908f64cd1c5c8b5d5c0b8e5e58fe313dbcf2589353671316a0b68",
    "instruction_count": 41,
    "instruction_bytes": 164,
    "body_bytes": 164,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5e390](../00c5e/00c5e390.md)

## 呼び出し先

- [00c5a870](../00c5a/00c5a870.md)
- [00c5b0a0](../00c5b/00c5b0a0.md)
- [00c5b130](../00c5b/00c5b130.md)
- [00c5b300](../00c5b/00c5b300.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5e620](../00c5e/00c5e620.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1248 bytes

~~~c

ulong _ZN8firebase9messaging17NotifyListenerSetEPNS0_8ListenerE(ulong param_1)

{
  int __fd;
  uint uVar1;
  byte *__filename;
  FILE *__stream;
  byte *__filename_00;
  
  if ((param_1 != 0) && (DAT_01127420 != 0)) {
    if ((*DAT_01127450 & 1) == 0) {
      __filename_00 = DAT_01127450 + 1;
    }
    else {
      __filename_00 = *(byte **)(DAT_01127450 + 0x10);
    }
    __fd = _ZN8firebase9messaging10FileLocker11AcquireLockEPKc(__filename_00);
    if ((*DAT_01127428 & 1) == 0) {
      __filename = DAT_01127428 + 1;
                    /* try { // try from 00bba814 to 00cba9ff has its CatchHandler @ 00bba814
                       catch() { ... } // from try @ 00bba814 with catch @ 00bba814
                       catch() { ... } // from try @ 00bbaa30 with catch @ 00bba814 */
    }
    else {
      __filename = *(byte **)(DAT_01127428 + 0x10);
    }
    __stream = fopen((char *)__filename,"a");
    param_1 = 0;
    if (__stream != (FILE *)0x0) {
      uVar1 = fclose(__stream);
      param_1 = (ulong)uVar1;
    }
    if (-1 < __fd) {
      remove((char *)__filename_00);
      close(__fd);
      param_1 = 0;
      if (DAT_01127418 != 0) {
        param_1 = _ZN8firebase5Mutex7ReleaseEv();
      }
    }
  }
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bba7bc"></a> `00bba7bc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bba7c0"></a> `00bba7c0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bba7c4"></a> `00bba7c4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bba7c8"></a> `00bba7c8` | `60 04 00 b4` | cbz x0,0x00bba854 | `CONDITIONAL_JUMP`
<a id="insn-00bba7cc"></a> `00bba7cc` | `68 2b 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bba7d0"></a> `00bba7d0` | `08 11 42 f9` | ldr x8,[x8, #0x420] | `FALL_THROUGH`
<a id="insn-00bba7d4"></a> `00bba7d4` | `08 04 00 b4` | cbz x8,0x00bba854 | `CONDITIONAL_JUMP`
<a id="insn-00bba7d8"></a> `00bba7d8` | `68 2b 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bba7dc"></a> `00bba7dc` | `08 29 42 f9` | ldr x8,[x8, #0x450] | `FALL_THROUGH`
<a id="insn-00bba7e0"></a> `00bba7e0` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bba7e4"></a> `00bba7e4` | `69 00 00 37` | tbnz w9,#0x0,0x00bba7f0 | `CONDITIONAL_JUMP`
<a id="insn-00bba7e8"></a> `00bba7e8` | `13 05 00 91` | add x19,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bba7ec"></a> `00bba7ec` | `02 00 00 14` | b 0x00bba7f4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bba7f0"></a> `00bba7f0` | `13 09 40 f9` | ldr x19,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bba7f4"></a> `00bba7f4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bba7f8"></a> `00bba7f8` | `8a 8f 02 94` | bl 0x00c5e620 | `UNCONDITIONAL_CALL`
<a id="insn-00bba7fc"></a> `00bba7fc` | `68 2b 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bba800"></a> `00bba800` | `08 15 42 f9` | ldr x8,[x8, #0x428] | `FALL_THROUGH`
<a id="insn-00bba804"></a> `00bba804` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bba808"></a> `00bba808` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bba80c"></a> `00bba80c` | `69 00 00 37` | tbnz w9,#0x0,0x00bba818 | `CONDITIONAL_JUMP`
<a id="insn-00bba810"></a> `00bba810` | `00 05 00 91` | add x0,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bba814"></a> `00bba814` | `02 00 00 14` | b 0x00bba81c | `UNCONDITIONAL_JUMP`
<a id="insn-00bba818"></a> `00bba818` | `00 09 40 f9` | ldr x0,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bba81c"></a> `00bba81c` | `41 b7 ff 90` | adrp x1,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bba820"></a> `00bba820` | `21 d4 06 91` | add x1,x1,#0x1b5 | `FALL_THROUGH`
<a id="insn-00bba824"></a> `00bba824` | `43 82 02 94` | bl 0x00c5b130 | `UNCONDITIONAL_CALL`
<a id="insn-00bba828"></a> `00bba828` | `40 00 00 b4` | cbz x0,0x00bba830 | `CONDITIONAL_JUMP`
<a id="insn-00bba82c"></a> `00bba82c` | `1d 82 02 94` | bl 0x00c5b0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bba830"></a> `00bba830` | `34 01 f8 37` | tbnz w20,#0x1f,0x00bba854 | `CONDITIONAL_JUMP`
<a id="insn-00bba834"></a> `00bba834` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bba838"></a> `00bba838` | `b2 82 02 94` | bl 0x00c5b300 | `UNCONDITIONAL_CALL`
<a id="insn-00bba83c"></a> `00bba83c` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00bba840"></a> `00bba840` | `0c 80 02 94` | bl 0x00c5a870 | `UNCONDITIONAL_CALL`
<a id="insn-00bba844"></a> `00bba844` | `68 2b 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bba848"></a> `00bba848` | `00 0d 42 f9` | ldr x0,[x8, #0x418] | `FALL_THROUGH`
<a id="insn-00bba84c"></a> `00bba84c` | `40 00 00 b4` | cbz x0,0x00bba854 | `CONDITIONAL_JUMP`
<a id="insn-00bba850"></a> `00bba850` | `98 84 02 94` | bl 0x00c5bab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bba854"></a> `00bba854` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bba858"></a> `00bba858` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bba85c"></a> `00bba85c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bba7bc`](#insn-00bba7bc) 範囲 `[['00bba7bc', '00bba7cb']]`
  - `CONDITIONAL_JUMP` [`00bba7c8`](#insn-00bba7c8) → [`00bba854`](#insn-00bba854)
  - `FALL_THROUGH` [`00bba7c8`](#insn-00bba7c8) → [`00bba7cc`](#insn-00bba7cc)
- ブロック [`00bba7cc`](#insn-00bba7cc) 範囲 `[['00bba7cc', '00bba7d7']]`
  - `CONDITIONAL_JUMP` [`00bba7d4`](#insn-00bba7d4) → [`00bba854`](#insn-00bba854)
  - `FALL_THROUGH` [`00bba7d4`](#insn-00bba7d4) → [`00bba7d8`](#insn-00bba7d8)
- ブロック [`00bba7d8`](#insn-00bba7d8) 範囲 `[['00bba7d8', '00bba7e7']]`
  - `CONDITIONAL_JUMP` [`00bba7e4`](#insn-00bba7e4) → [`00bba7f0`](#insn-00bba7f0)
  - `FALL_THROUGH` [`00bba7e4`](#insn-00bba7e4) → [`00bba7e8`](#insn-00bba7e8)
- ブロック [`00bba7e8`](#insn-00bba7e8) 範囲 `[['00bba7e8', '00bba7ef']]`
  - `UNCONDITIONAL_JUMP` [`00bba7ec`](#insn-00bba7ec) → [`00bba7f4`](#insn-00bba7f4)
- ブロック [`00bba7f0`](#insn-00bba7f0) 範囲 `[['00bba7f0', '00bba7f3']]`
  - `FALL_THROUGH` [`00bba7f0`](#insn-00bba7f0) → [`00bba7f4`](#insn-00bba7f4)
- ブロック [`00bba7f4`](#insn-00bba7f4) 範囲 `[['00bba7f4', '00bba80f']]`
  - `CONDITIONAL_JUMP` [`00bba80c`](#insn-00bba80c) → [`00bba818`](#insn-00bba818)
  - `FALL_THROUGH` [`00bba80c`](#insn-00bba80c) → [`00bba810`](#insn-00bba810)
- ブロック [`00bba810`](#insn-00bba810) 範囲 `[['00bba810', '00bba813']]`
  - `FALL_THROUGH` [`00bba810`](#insn-00bba810) → [`00bba814`](#insn-00bba814)
- ブロック [`00bba814`](#insn-00bba814) 範囲 `[['00bba814', '00bba817']]`
  - `UNCONDITIONAL_JUMP` [`00bba814`](#insn-00bba814) → [`00bba81c`](#insn-00bba81c)
- ブロック [`00bba818`](#insn-00bba818) 範囲 `[['00bba818', '00bba81b']]`
  - `FALL_THROUGH` [`00bba818`](#insn-00bba818) → [`00bba81c`](#insn-00bba81c)
- ブロック [`00bba81c`](#insn-00bba81c) 範囲 `[['00bba81c', '00bba82b']]`
  - `CONDITIONAL_JUMP` [`00bba828`](#insn-00bba828) → [`00bba830`](#insn-00bba830)
  - `FALL_THROUGH` [`00bba828`](#insn-00bba828) → [`00bba82c`](#insn-00bba82c)
- ブロック [`00bba82c`](#insn-00bba82c) 範囲 `[['00bba82c', '00bba82f']]`
  - `FALL_THROUGH` [`00bba82c`](#insn-00bba82c) → [`00bba830`](#insn-00bba830)
- ブロック [`00bba830`](#insn-00bba830) 範囲 `[['00bba830', '00bba833']]`
  - `CONDITIONAL_JUMP` [`00bba830`](#insn-00bba830) → [`00bba854`](#insn-00bba854)
  - `FALL_THROUGH` [`00bba830`](#insn-00bba830) → [`00bba834`](#insn-00bba834)
- ブロック [`00bba834`](#insn-00bba834) 範囲 `[['00bba834', '00bba84f']]`
  - `CONDITIONAL_JUMP` [`00bba84c`](#insn-00bba84c) → [`00bba854`](#insn-00bba854)
  - `FALL_THROUGH` [`00bba84c`](#insn-00bba84c) → [`00bba850`](#insn-00bba850)
- ブロック [`00bba850`](#insn-00bba850) 範囲 `[['00bba850', '00bba853']]`
  - `FALL_THROUGH` [`00bba850`](#insn-00bba850) → [`00bba854`](#insn-00bba854)
- ブロック [`00bba854`](#insn-00bba854) 範囲 `[['00bba854', '00bba85f']]`

## 命令位置別の参照

- [`00bba7bc`](#insn-00bba7bc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba7c0`](#insn-00bba7c0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba7c8`](#insn-00bba7c8) → [`00bba854`](#insn-00bba854) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba7d0`](#insn-00bba7d0) → `01127420`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bba7d4`](#insn-00bba7d4) → [`00bba854`](#insn-00bba854) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba7dc`](#insn-00bba7dc) → `01127450`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bba7e4`](#insn-00bba7e4) → [`00bba7f0`](#insn-00bba7f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba7ec`](#insn-00bba7ec) → [`00bba7f4`](#insn-00bba7f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba7f8`](#insn-00bba7f8) → [`00c5e620`](../00c5e/00c5e620.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e620` · 推定シンボル `None` · 推定型 `None`
- [`00bba800`](#insn-00bba800) → `01127428`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bba80c`](#insn-00bba80c) → [`00bba818`](#insn-00bba818) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba814`](#insn-00bba814) → [`00bba81c`](#insn-00bba81c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba820`](#insn-00bba820) → `002a21b5`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba824`](#insn-00bba824) → [`00c5b130`](../00c5b/00c5b130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b130` · 推定シンボル `None` · 推定型 `None`
- [`00bba828`](#insn-00bba828) → [`00bba830`](#insn-00bba830) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba82c`](#insn-00bba82c) → [`00c5b0a0`](../00c5b/00c5b0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bba830`](#insn-00bba830) → [`00bba854`](#insn-00bba854) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba838`](#insn-00bba838) → [`00c5b300`](../00c5b/00c5b300.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b300` · 推定シンボル `None` · 推定型 `None`
- [`00bba840`](#insn-00bba840) → [`00c5a870`](../00c5a/00c5a870.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a870` · 推定シンボル `None` · 推定型 `None`
- [`00bba848`](#insn-00bba848) → `01127418`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bba84c`](#insn-00bba84c) → [`00bba854`](#insn-00bba854) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba850`](#insn-00bba850) → [`00c5bab0`](../00c5b/00c5bab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bab0` · 推定シンボル `None` · 推定型 `None`
- [`00bba854`](#insn-00bba854) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bba7bc`](#insn-00bba7bc)

~~~json
{
  "source": "00bba7bc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba7c0`](#insn-00bba7c0)

~~~json
{
  "source": "00bba7c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba7c8`](#insn-00bba7c8)

~~~json
{
  "source": "00bba7c8",
  "target": "00bba854",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba7d0`](#insn-00bba7d0)

~~~json
{
  "source": "00bba7d0",
  "target": "01127420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127420",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bba7d4`](#insn-00bba7d4)

~~~json
{
  "source": "00bba7d4",
  "target": "00bba854",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba7dc`](#insn-00bba7dc)

~~~json
{
  "source": "00bba7dc",
  "target": "01127450",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127450",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bba7e4`](#insn-00bba7e4)

~~~json
{
  "source": "00bba7e4",
  "target": "00bba7f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba7ec`](#insn-00bba7ec)

~~~json
{
  "source": "00bba7ec",
  "target": "00bba7f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba7f8`](#insn-00bba7f8)

~~~json
{
  "source": "00bba7f8",
  "target": "00c5e620",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba800`](#insn-00bba800)

~~~json
{
  "source": "00bba800",
  "target": "01127428",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127428",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bba80c`](#insn-00bba80c)

~~~json
{
  "source": "00bba80c",
  "target": "00bba818",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba814`](#insn-00bba814)

~~~json
{
  "source": "00bba814",
  "target": "00bba81c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba820`](#insn-00bba820)

~~~json
{
  "source": "00bba820",
  "target": "002a21b5",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba824`](#insn-00bba824)

~~~json
{
  "source": "00bba824",
  "target": "00c5b130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba828`](#insn-00bba828)

~~~json
{
  "source": "00bba828",
  "target": "00bba830",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba82c`](#insn-00bba82c)

~~~json
{
  "source": "00bba82c",
  "target": "00c5b0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba830`](#insn-00bba830)

~~~json
{
  "source": "00bba830",
  "target": "00bba854",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba838`](#insn-00bba838)

~~~json
{
  "source": "00bba838",
  "target": "00c5b300",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba840`](#insn-00bba840)

~~~json
{
  "source": "00bba840",
  "target": "00c5a870",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba848`](#insn-00bba848)

~~~json
{
  "source": "00bba848",
  "target": "01127418",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127418",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bba84c`](#insn-00bba84c)

~~~json
{
  "source": "00bba84c",
  "target": "00bba854",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba850`](#insn-00bba850)

~~~json
{
  "source": "00bba850",
  "target": "00c5bab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba854`](#insn-00bba854)

~~~json
{
  "source": "00bba854",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
