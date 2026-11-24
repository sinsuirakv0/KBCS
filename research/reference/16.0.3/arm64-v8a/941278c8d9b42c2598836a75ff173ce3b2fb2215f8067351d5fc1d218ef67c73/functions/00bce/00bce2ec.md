# 00bce2ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcd2f8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd2f8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-be4566c47d4c3bb244b48c2afa92594d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bce2ec",
  "name": "_ZN8firebase4auth18ReleaseAuthClassesEP7_JNIEnv",
  "size": 340,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1809b594c92d159fa08976a23ff4588d4727346f2c0768a581423bdd9b28365b",
  "source_text_sha256": "1809b594c92d159fa08976a23ff4588d4727346f2c0768a581423bdd9b28365b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bce2ec",
        "00bce43f"
      ]
    ],
    "bytes_sha256": "d474c9661c4e47e51f62921f7208a6b1095104920d9ebf0ff40bf6cd38425bed",
    "instruction_count": 85,
    "instruction_bytes": 340,
    "body_bytes": 340,
    "indirect": 8,
    "unresolved": 8
  }
}
~~~

## 呼び出し元

- [00c5ed00](../00c5e/00c5ed00.md)

## 呼び出し先

- [00c5c000](../00c5c/00c5c000.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1746 bytes

~~~c

void _ZN8firebase4auth18ReleaseAuthClassesEP7_JNIEnv(long *param_1)

{
  if (DAT_011277e8 != 0) {
                    /* try { // try from 00bce314 to 00cce32b has its CatchHandler @ 00bcf9ac */
    if (DAT_011277f0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011277f0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
                    /* try { // try from 00bce334 to 00cce347 has its CatchHandler @ 00bcf950 */
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011277e8);
    DAT_011277e8 = 0;
  }
  if (DAT_01127890 != 0) {
    if (DAT_01127898 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01127898 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01127890);
                    /* try { // try from 00bce394 to 00cce39f has its CatchHandler @ 00bcfa08 */
    DAT_01127890 = 0;
  }
                    /* try { // try from 00bce3a0 to 00cce42b has its CatchHandler @ 00bcd634 */
  if (DAT_011278b0 != 0) {
    if (DAT_011278b8 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011278b8 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011278b0);
    DAT_011278b0 = 0;
  }
  if (DAT_011278d8 != 0) {
    if (DAT_011278e0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011278e0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011278d8);
                    /* try { // try from 00bce42c to 00cce437 has its CatchHandler @ 00bcf9b0 */
    DAT_011278d8 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bce2ec"></a> `00bce2ec` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bce2f0"></a> `00bce2f0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bce2f4"></a> `00bce2f4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bce2f8"></a> `00bce2f8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bce2fc"></a> `00bce2fc` | `d4 2a 00 b0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bce300"></a> `00bce300` | `81 f6 43 f9` | ldr x1,[x20, #0x7e8] | `FALL_THROUGH`
<a id="insn-00bce304"></a> `00bce304` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bce308"></a> `00bce308` | `21 02 00 b4` | cbz x1,0x00bce34c | `CONDITIONAL_JUMP`
<a id="insn-00bce30c"></a> `00bce30c` | `d5 2a 00 b0` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bce310"></a> `00bce310` | `a8 c2 5f 39` | ldrb w8,[x21, #0x7f0] | `FALL_THROUGH`
<a id="insn-00bce314"></a> `00bce314` | `c8 00 00 34` | cbz w8,0x00bce32c | `CONDITIONAL_JUMP`
<a id="insn-00bce318"></a> `00bce318` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bce31c"></a> `00bce31c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce320"></a> `00bce320` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bce324"></a> `00bce324` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bce328"></a> `00bce328` | `bf c2 1f 39` | strb wzr,[x21, #0x7f0] | `FALL_THROUGH`
<a id="insn-00bce32c"></a> `00bce32c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce330"></a> `00bce330` | `34 37 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bce334"></a> `00bce334` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bce338"></a> `00bce338` | `81 f6 43 f9` | ldr x1,[x20, #0x7e8] | `FALL_THROUGH`
<a id="insn-00bce33c"></a> `00bce33c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce340"></a> `00bce340` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bce344"></a> `00bce344` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bce348"></a> `00bce348` | `9f f6 03 f9` | str xzr,[x20, #0x7e8] | `FALL_THROUGH`
<a id="insn-00bce34c"></a> `00bce34c` | `d4 2a 00 b0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bce350"></a> `00bce350` | `81 4a 44 f9` | ldr x1,[x20, #0x890] | `FALL_THROUGH`
<a id="insn-00bce354"></a> `00bce354` | `21 02 00 b4` | cbz x1,0x00bce398 | `CONDITIONAL_JUMP`
<a id="insn-00bce358"></a> `00bce358` | `d5 2a 00 b0` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bce35c"></a> `00bce35c` | `a8 62 62 39` | ldrb w8,[x21, #0x898] | `FALL_THROUGH`
<a id="insn-00bce360"></a> `00bce360` | `c8 00 00 34` | cbz w8,0x00bce378 | `CONDITIONAL_JUMP`
<a id="insn-00bce364"></a> `00bce364` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bce368"></a> `00bce368` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce36c"></a> `00bce36c` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bce370"></a> `00bce370` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bce374"></a> `00bce374` | `bf 62 22 39` | strb wzr,[x21, #0x898] | `FALL_THROUGH`
<a id="insn-00bce378"></a> `00bce378` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce37c"></a> `00bce37c` | `21 37 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bce380"></a> `00bce380` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bce384"></a> `00bce384` | `81 4a 44 f9` | ldr x1,[x20, #0x890] | `FALL_THROUGH`
<a id="insn-00bce388"></a> `00bce388` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce38c"></a> `00bce38c` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bce390"></a> `00bce390` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bce394"></a> `00bce394` | `9f 4a 04 f9` | str xzr,[x20, #0x890] | `FALL_THROUGH`
<a id="insn-00bce398"></a> `00bce398` | `d4 2a 00 b0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bce39c"></a> `00bce39c` | `81 5a 44 f9` | ldr x1,[x20, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bce3a0"></a> `00bce3a0` | `21 02 00 b4` | cbz x1,0x00bce3e4 | `CONDITIONAL_JUMP`
<a id="insn-00bce3a4"></a> `00bce3a4` | `d5 2a 00 b0` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bce3a8"></a> `00bce3a8` | `a8 e2 62 39` | ldrb w8,[x21, #0x8b8] | `FALL_THROUGH`
<a id="insn-00bce3ac"></a> `00bce3ac` | `c8 00 00 34` | cbz w8,0x00bce3c4 | `CONDITIONAL_JUMP`
<a id="insn-00bce3b0"></a> `00bce3b0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bce3b4"></a> `00bce3b4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce3b8"></a> `00bce3b8` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bce3bc"></a> `00bce3bc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bce3c0"></a> `00bce3c0` | `bf e2 22 39` | strb wzr,[x21, #0x8b8] | `FALL_THROUGH`
<a id="insn-00bce3c4"></a> `00bce3c4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce3c8"></a> `00bce3c8` | `0e 37 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bce3cc"></a> `00bce3cc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bce3d0"></a> `00bce3d0` | `81 5a 44 f9` | ldr x1,[x20, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bce3d4"></a> `00bce3d4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce3d8"></a> `00bce3d8` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bce3dc"></a> `00bce3dc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bce3e0"></a> `00bce3e0` | `9f 5a 04 f9` | str xzr,[x20, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bce3e4"></a> `00bce3e4` | `d4 2a 00 b0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bce3e8"></a> `00bce3e8` | `81 6e 44 f9` | ldr x1,[x20, #0x8d8] | `FALL_THROUGH`
<a id="insn-00bce3ec"></a> `00bce3ec` | `21 02 00 b4` | cbz x1,0x00bce430 | `CONDITIONAL_JUMP`
<a id="insn-00bce3f0"></a> `00bce3f0` | `d5 2a 00 b0` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bce3f4"></a> `00bce3f4` | `a8 82 63 39` | ldrb w8,[x21, #0x8e0] | `FALL_THROUGH`
<a id="insn-00bce3f8"></a> `00bce3f8` | `c8 00 00 34` | cbz w8,0x00bce410 | `CONDITIONAL_JUMP`
<a id="insn-00bce3fc"></a> `00bce3fc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bce400"></a> `00bce400` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce404"></a> `00bce404` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bce408"></a> `00bce408` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bce40c"></a> `00bce40c` | `bf 82 23 39` | strb wzr,[x21, #0x8e0] | `FALL_THROUGH`
<a id="insn-00bce410"></a> `00bce410` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce414"></a> `00bce414` | `fb 36 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bce418"></a> `00bce418` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bce41c"></a> `00bce41c` | `81 6e 44 f9` | ldr x1,[x20, #0x8d8] | `FALL_THROUGH`
<a id="insn-00bce420"></a> `00bce420` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce424"></a> `00bce424` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bce428"></a> `00bce428` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bce42c"></a> `00bce42c` | `9f 6e 04 f9` | str xzr,[x20, #0x8d8] | `FALL_THROUGH`
<a id="insn-00bce430"></a> `00bce430` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bce434"></a> `00bce434` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bce438"></a> `00bce438` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bce43c"></a> `00bce43c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bce2ec`](#insn-00bce2ec) 範囲 `[['00bce2ec', '00bce30b']]`
  - `CONDITIONAL_JUMP` [`00bce308`](#insn-00bce308) → [`00bce34c`](#insn-00bce34c)
  - `FALL_THROUGH` [`00bce308`](#insn-00bce308) → [`00bce30c`](#insn-00bce30c)
- ブロック [`00bce30c`](#insn-00bce30c) 範囲 `[['00bce30c', '00bce313']]`
  - `FALL_THROUGH` [`00bce310`](#insn-00bce310) → [`00bce314`](#insn-00bce314)
- ブロック [`00bce314`](#insn-00bce314) 範囲 `[['00bce314', '00bce317']]`
  - `CONDITIONAL_JUMP` [`00bce314`](#insn-00bce314) → [`00bce32c`](#insn-00bce32c)
  - `FALL_THROUGH` [`00bce314`](#insn-00bce314) → [`00bce318`](#insn-00bce318)
- ブロック [`00bce318`](#insn-00bce318) 範囲 `[['00bce318', '00bce32b']]`
  - `FALL_THROUGH` [`00bce328`](#insn-00bce328) → [`00bce32c`](#insn-00bce32c)
- ブロック [`00bce32c`](#insn-00bce32c) 範囲 `[['00bce32c', '00bce333']]`
  - `FALL_THROUGH` [`00bce330`](#insn-00bce330) → [`00bce334`](#insn-00bce334)
- ブロック [`00bce334`](#insn-00bce334) 範囲 `[['00bce334', '00bce34b']]`
  - `FALL_THROUGH` [`00bce348`](#insn-00bce348) → [`00bce34c`](#insn-00bce34c)
- ブロック [`00bce34c`](#insn-00bce34c) 範囲 `[['00bce34c', '00bce357']]`
  - `CONDITIONAL_JUMP` [`00bce354`](#insn-00bce354) → [`00bce398`](#insn-00bce398)
  - `FALL_THROUGH` [`00bce354`](#insn-00bce354) → [`00bce358`](#insn-00bce358)
- ブロック [`00bce358`](#insn-00bce358) 範囲 `[['00bce358', '00bce363']]`
  - `CONDITIONAL_JUMP` [`00bce360`](#insn-00bce360) → [`00bce378`](#insn-00bce378)
  - `FALL_THROUGH` [`00bce360`](#insn-00bce360) → [`00bce364`](#insn-00bce364)
- ブロック [`00bce364`](#insn-00bce364) 範囲 `[['00bce364', '00bce377']]`
  - `FALL_THROUGH` [`00bce374`](#insn-00bce374) → [`00bce378`](#insn-00bce378)
- ブロック [`00bce378`](#insn-00bce378) 範囲 `[['00bce378', '00bce393']]`
  - `FALL_THROUGH` [`00bce390`](#insn-00bce390) → [`00bce394`](#insn-00bce394)
- ブロック [`00bce394`](#insn-00bce394) 範囲 `[['00bce394', '00bce397']]`
  - `FALL_THROUGH` [`00bce394`](#insn-00bce394) → [`00bce398`](#insn-00bce398)
- ブロック [`00bce398`](#insn-00bce398) 範囲 `[['00bce398', '00bce39f']]`
  - `FALL_THROUGH` [`00bce39c`](#insn-00bce39c) → [`00bce3a0`](#insn-00bce3a0)
- ブロック [`00bce3a0`](#insn-00bce3a0) 範囲 `[['00bce3a0', '00bce3a3']]`
  - `CONDITIONAL_JUMP` [`00bce3a0`](#insn-00bce3a0) → [`00bce3e4`](#insn-00bce3e4)
  - `FALL_THROUGH` [`00bce3a0`](#insn-00bce3a0) → [`00bce3a4`](#insn-00bce3a4)
- ブロック [`00bce3a4`](#insn-00bce3a4) 範囲 `[['00bce3a4', '00bce3af']]`
  - `CONDITIONAL_JUMP` [`00bce3ac`](#insn-00bce3ac) → [`00bce3c4`](#insn-00bce3c4)
  - `FALL_THROUGH` [`00bce3ac`](#insn-00bce3ac) → [`00bce3b0`](#insn-00bce3b0)
- ブロック [`00bce3b0`](#insn-00bce3b0) 範囲 `[['00bce3b0', '00bce3c3']]`
  - `FALL_THROUGH` [`00bce3c0`](#insn-00bce3c0) → [`00bce3c4`](#insn-00bce3c4)
- ブロック [`00bce3c4`](#insn-00bce3c4) 範囲 `[['00bce3c4', '00bce3e3']]`
  - `FALL_THROUGH` [`00bce3e0`](#insn-00bce3e0) → [`00bce3e4`](#insn-00bce3e4)
- ブロック [`00bce3e4`](#insn-00bce3e4) 範囲 `[['00bce3e4', '00bce3ef']]`
  - `CONDITIONAL_JUMP` [`00bce3ec`](#insn-00bce3ec) → [`00bce430`](#insn-00bce430)
  - `FALL_THROUGH` [`00bce3ec`](#insn-00bce3ec) → [`00bce3f0`](#insn-00bce3f0)
- ブロック [`00bce3f0`](#insn-00bce3f0) 範囲 `[['00bce3f0', '00bce3fb']]`
  - `CONDITIONAL_JUMP` [`00bce3f8`](#insn-00bce3f8) → [`00bce410`](#insn-00bce410)
  - `FALL_THROUGH` [`00bce3f8`](#insn-00bce3f8) → [`00bce3fc`](#insn-00bce3fc)
- ブロック [`00bce3fc`](#insn-00bce3fc) 範囲 `[['00bce3fc', '00bce40f']]`
  - `FALL_THROUGH` [`00bce40c`](#insn-00bce40c) → [`00bce410`](#insn-00bce410)
- ブロック [`00bce410`](#insn-00bce410) 範囲 `[['00bce410', '00bce42b']]`
  - `FALL_THROUGH` [`00bce428`](#insn-00bce428) → [`00bce42c`](#insn-00bce42c)
- ブロック [`00bce42c`](#insn-00bce42c) 範囲 `[['00bce42c', '00bce42f']]`
  - `FALL_THROUGH` [`00bce42c`](#insn-00bce42c) → [`00bce430`](#insn-00bce430)
- ブロック [`00bce430`](#insn-00bce430) 範囲 `[['00bce430', '00bce43f']]`

## 命令位置別の参照

- [`00bce2ec`](#insn-00bce2ec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce2f0`](#insn-00bce2f0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce2f4`](#insn-00bce2f4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce300`](#insn-00bce300) → `011277e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce308`](#insn-00bce308) → [`00bce34c`](#insn-00bce34c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce310`](#insn-00bce310) → `011277f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bce314`](#insn-00bce314) → [`00bce32c`](#insn-00bce32c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce328`](#insn-00bce328) → `011277f0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bce330`](#insn-00bce330) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bce338`](#insn-00bce338) → `011277e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce348`](#insn-00bce348) → `011277e8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce350`](#insn-00bce350) → `01127890`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce354`](#insn-00bce354) → [`00bce398`](#insn-00bce398) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce35c`](#insn-00bce35c) → `01127898`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bce360`](#insn-00bce360) → [`00bce378`](#insn-00bce378) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce374`](#insn-00bce374) → `01127898`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bce37c`](#insn-00bce37c) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bce384`](#insn-00bce384) → `01127890`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce394`](#insn-00bce394) → `01127890`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce39c`](#insn-00bce39c) → `011278b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce3a0`](#insn-00bce3a0) → [`00bce3e4`](#insn-00bce3e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce3a8`](#insn-00bce3a8) → `011278b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bce3ac`](#insn-00bce3ac) → [`00bce3c4`](#insn-00bce3c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce3c0`](#insn-00bce3c0) → `011278b8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bce3c8`](#insn-00bce3c8) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bce3d0`](#insn-00bce3d0) → `011278b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce3e0`](#insn-00bce3e0) → `011278b0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce3e8`](#insn-00bce3e8) → `011278d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce3ec`](#insn-00bce3ec) → [`00bce430`](#insn-00bce430) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce3f4`](#insn-00bce3f4) → `011278e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bce3f8`](#insn-00bce3f8) → [`00bce410`](#insn-00bce410) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce40c`](#insn-00bce40c) → `011278e0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bce414`](#insn-00bce414) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bce41c`](#insn-00bce41c) → `011278d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce42c`](#insn-00bce42c) → `011278d8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce430`](#insn-00bce430) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce434`](#insn-00bce434) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bce2ec`](#insn-00bce2ec)

~~~json
{
  "source": "00bce2ec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce2f0`](#insn-00bce2f0)

~~~json
{
  "source": "00bce2f0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce2f4`](#insn-00bce2f4)

~~~json
{
  "source": "00bce2f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce300`](#insn-00bce300)

~~~json
{
  "source": "00bce300",
  "target": "011277e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011277e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce308`](#insn-00bce308)

~~~json
{
  "source": "00bce308",
  "target": "00bce34c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce310`](#insn-00bce310)

~~~json
{
  "source": "00bce310",
  "target": "011277f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011277f0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce314`](#insn-00bce314)

~~~json
{
  "source": "00bce314",
  "target": "00bce32c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce328`](#insn-00bce328)

~~~json
{
  "source": "00bce328",
  "target": "011277f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011277f0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce330`](#insn-00bce330)

~~~json
{
  "source": "00bce330",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce338`](#insn-00bce338)

~~~json
{
  "source": "00bce338",
  "target": "011277e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011277e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce348`](#insn-00bce348)

~~~json
{
  "source": "00bce348",
  "target": "011277e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011277e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce350`](#insn-00bce350)

~~~json
{
  "source": "00bce350",
  "target": "01127890",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127890",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce354`](#insn-00bce354)

~~~json
{
  "source": "00bce354",
  "target": "00bce398",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce35c`](#insn-00bce35c)

~~~json
{
  "source": "00bce35c",
  "target": "01127898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127898",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce360`](#insn-00bce360)

~~~json
{
  "source": "00bce360",
  "target": "00bce378",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce374`](#insn-00bce374)

~~~json
{
  "source": "00bce374",
  "target": "01127898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127898",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce37c`](#insn-00bce37c)

~~~json
{
  "source": "00bce37c",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce384`](#insn-00bce384)

~~~json
{
  "source": "00bce384",
  "target": "01127890",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127890",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce394`](#insn-00bce394)

~~~json
{
  "source": "00bce394",
  "target": "01127890",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127890",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce39c`](#insn-00bce39c)

~~~json
{
  "source": "00bce39c",
  "target": "011278b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce3a0`](#insn-00bce3a0)

~~~json
{
  "source": "00bce3a0",
  "target": "00bce3e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce3a8`](#insn-00bce3a8)

~~~json
{
  "source": "00bce3a8",
  "target": "011278b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278b8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce3ac`](#insn-00bce3ac)

~~~json
{
  "source": "00bce3ac",
  "target": "00bce3c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce3c0`](#insn-00bce3c0)

~~~json
{
  "source": "00bce3c0",
  "target": "011278b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278b8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce3c8`](#insn-00bce3c8)

~~~json
{
  "source": "00bce3c8",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce3d0`](#insn-00bce3d0)

~~~json
{
  "source": "00bce3d0",
  "target": "011278b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce3e0`](#insn-00bce3e0)

~~~json
{
  "source": "00bce3e0",
  "target": "011278b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce3e8`](#insn-00bce3e8)

~~~json
{
  "source": "00bce3e8",
  "target": "011278d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce3ec`](#insn-00bce3ec)

~~~json
{
  "source": "00bce3ec",
  "target": "00bce430",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce3f4`](#insn-00bce3f4)

~~~json
{
  "source": "00bce3f4",
  "target": "011278e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278e0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce3f8`](#insn-00bce3f8)

~~~json
{
  "source": "00bce3f8",
  "target": "00bce410",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce40c`](#insn-00bce40c)

~~~json
{
  "source": "00bce40c",
  "target": "011278e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278e0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce414`](#insn-00bce414)

~~~json
{
  "source": "00bce414",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce41c`](#insn-00bce41c)

~~~json
{
  "source": "00bce41c",
  "target": "011278d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce42c`](#insn-00bce42c)

~~~json
{
  "source": "00bce42c",
  "target": "011278d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce430`](#insn-00bce430)

~~~json
{
  "source": "00bce430",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce434`](#insn-00bce434)

~~~json
{
  "source": "00bce434",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
