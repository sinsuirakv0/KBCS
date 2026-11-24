# 00bdf0fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bde108`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde108.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-af84ab670b729cf297d45e6c5dafcbf0)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdf0fc",
  "name": "_ZN8firebase4auth18ReleaseUserClassesEP7_JNIEnv",
  "size": 416,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bbf5b7f51af542bf84fa86114c26cf2ec725b0d29759004f9df1cc47e8b10519",
  "source_text_sha256": "bbf5b7f51af542bf84fa86114c26cf2ec725b0d29759004f9df1cc47e8b10519",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdf0fc",
        "00bdf29b"
      ]
    ],
    "bytes_sha256": "2b245570cd81f065ba3ef2c7f67029fcf75a23885ce2210d459301040690d02b",
    "instruction_count": 104,
    "instruction_bytes": 416,
    "body_bytes": 416,
    "indirect": 10,
    "unresolved": 10
  }
}
~~~

## 呼び出し元

- [00c5ed10](../00c5e/00c5ed10.md)

## 呼び出し先

- [00c5c000](../00c5c/00c5c000.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1555 bytes

~~~c

void _ZN8firebase4auth18ReleaseUserClassesEP7_JNIEnv(long *param_1)

{
  if (DAT_01127dc0 != 0) {
    if (DAT_01127dc8 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01127dc8 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01127dc0);
    DAT_01127dc0 = 0;
  }
  if (DAT_01127de0 != 0) {
    if (DAT_01127de8 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01127de8 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01127de0);
    DAT_01127de0 = 0;
  }
  if (DAT_01127e70 != 0) {
    if (DAT_01127e78 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01127e78 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01127e70);
    DAT_01127e70 = 0;
  }
  if (DAT_01127ec0 != 0) {
    if (DAT_01127ec8 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01127ec8 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01127ec0);
    DAT_01127ec0 = 0;
  }
  if (DAT_01127ee8 != 0) {
    if (DAT_01127ef0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01127ef0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01127ee8);
    DAT_01127ee8 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdf0fc"></a> `00bdf0fc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bdf100"></a> `00bdf100` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf104"></a> `00bdf104` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdf108"></a> `00bdf108` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdf10c"></a> `00bdf10c` | `54 2a 00 90` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdf110"></a> `00bdf110` | `81 e2 46 f9` | ldr x1,[x20, #0xdc0] | `FALL_THROUGH`
<a id="insn-00bdf114"></a> `00bdf114` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdf118"></a> `00bdf118` | `21 02 00 b4` | cbz x1,0x00bdf15c | `CONDITIONAL_JUMP`
<a id="insn-00bdf11c"></a> `00bdf11c` | `55 2a 00 90` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdf120"></a> `00bdf120` | `a8 22 77 39` | ldrb w8,[x21, #0xdc8] | `FALL_THROUGH`
<a id="insn-00bdf124"></a> `00bdf124` | `c8 00 00 34` | cbz w8,0x00bdf13c | `CONDITIONAL_JUMP`
<a id="insn-00bdf128"></a> `00bdf128` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdf12c"></a> `00bdf12c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdf130"></a> `00bdf130` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bdf134"></a> `00bdf134` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdf138"></a> `00bdf138` | `bf 22 37 39` | strb wzr,[x21, #0xdc8] | `FALL_THROUGH`
<a id="insn-00bdf13c"></a> `00bdf13c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdf140"></a> `00bdf140` | `b0 f3 01 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf144"></a> `00bdf144` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdf148"></a> `00bdf148` | `81 e2 46 f9` | ldr x1,[x20, #0xdc0] | `FALL_THROUGH`
<a id="insn-00bdf14c"></a> `00bdf14c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdf150"></a> `00bdf150` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdf154"></a> `00bdf154` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdf158"></a> `00bdf158` | `9f e2 06 f9` | str xzr,[x20, #0xdc0] | `FALL_THROUGH`
<a id="insn-00bdf15c"></a> `00bdf15c` | `54 2a 00 90` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdf160"></a> `00bdf160` | `81 f2 46 f9` | ldr x1,[x20, #0xde0] | `FALL_THROUGH`
<a id="insn-00bdf164"></a> `00bdf164` | `21 02 00 b4` | cbz x1,0x00bdf1a8 | `CONDITIONAL_JUMP`
<a id="insn-00bdf168"></a> `00bdf168` | `55 2a 00 90` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdf16c"></a> `00bdf16c` | `a8 a2 77 39` | ldrb w8,[x21, #0xde8] | `FALL_THROUGH`
<a id="insn-00bdf170"></a> `00bdf170` | `c8 00 00 34` | cbz w8,0x00bdf188 | `CONDITIONAL_JUMP`
<a id="insn-00bdf174"></a> `00bdf174` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdf178"></a> `00bdf178` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdf17c"></a> `00bdf17c` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bdf180"></a> `00bdf180` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdf184"></a> `00bdf184` | `bf a2 37 39` | strb wzr,[x21, #0xde8] | `FALL_THROUGH`
<a id="insn-00bdf188"></a> `00bdf188` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdf18c"></a> `00bdf18c` | `9d f3 01 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf190"></a> `00bdf190` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdf194"></a> `00bdf194` | `81 f2 46 f9` | ldr x1,[x20, #0xde0] | `FALL_THROUGH`
<a id="insn-00bdf198"></a> `00bdf198` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdf19c"></a> `00bdf19c` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdf1a0"></a> `00bdf1a0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdf1a4"></a> `00bdf1a4` | `9f f2 06 f9` | str xzr,[x20, #0xde0] | `FALL_THROUGH`
<a id="insn-00bdf1a8"></a> `00bdf1a8` | `54 2a 00 90` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdf1ac"></a> `00bdf1ac` | `81 3a 47 f9` | ldr x1,[x20, #0xe70] | `FALL_THROUGH`
<a id="insn-00bdf1b0"></a> `00bdf1b0` | `21 02 00 b4` | cbz x1,0x00bdf1f4 | `CONDITIONAL_JUMP`
<a id="insn-00bdf1b4"></a> `00bdf1b4` | `55 2a 00 90` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdf1b8"></a> `00bdf1b8` | `a8 e2 79 39` | ldrb w8,[x21, #0xe78] | `FALL_THROUGH`
<a id="insn-00bdf1bc"></a> `00bdf1bc` | `c8 00 00 34` | cbz w8,0x00bdf1d4 | `CONDITIONAL_JUMP`
<a id="insn-00bdf1c0"></a> `00bdf1c0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdf1c4"></a> `00bdf1c4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdf1c8"></a> `00bdf1c8` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bdf1cc"></a> `00bdf1cc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdf1d0"></a> `00bdf1d0` | `bf e2 39 39` | strb wzr,[x21, #0xe78] | `FALL_THROUGH`
<a id="insn-00bdf1d4"></a> `00bdf1d4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdf1d8"></a> `00bdf1d8` | `8a f3 01 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf1dc"></a> `00bdf1dc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdf1e0"></a> `00bdf1e0` | `81 3a 47 f9` | ldr x1,[x20, #0xe70] | `FALL_THROUGH`
<a id="insn-00bdf1e4"></a> `00bdf1e4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdf1e8"></a> `00bdf1e8` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdf1ec"></a> `00bdf1ec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdf1f0"></a> `00bdf1f0` | `9f 3a 07 f9` | str xzr,[x20, #0xe70] | `FALL_THROUGH`
<a id="insn-00bdf1f4"></a> `00bdf1f4` | `54 2a 00 90` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdf1f8"></a> `00bdf1f8` | `81 62 47 f9` | ldr x1,[x20, #0xec0] | `FALL_THROUGH`
<a id="insn-00bdf1fc"></a> `00bdf1fc` | `21 02 00 b4` | cbz x1,0x00bdf240 | `CONDITIONAL_JUMP`
<a id="insn-00bdf200"></a> `00bdf200` | `55 2a 00 90` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdf204"></a> `00bdf204` | `a8 22 7b 39` | ldrb w8,[x21, #0xec8] | `FALL_THROUGH`
<a id="insn-00bdf208"></a> `00bdf208` | `c8 00 00 34` | cbz w8,0x00bdf220 | `CONDITIONAL_JUMP`
<a id="insn-00bdf20c"></a> `00bdf20c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdf210"></a> `00bdf210` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdf214"></a> `00bdf214` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bdf218"></a> `00bdf218` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdf21c"></a> `00bdf21c` | `bf 22 3b 39` | strb wzr,[x21, #0xec8] | `FALL_THROUGH`
<a id="insn-00bdf220"></a> `00bdf220` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdf224"></a> `00bdf224` | `77 f3 01 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf228"></a> `00bdf228` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdf22c"></a> `00bdf22c` | `81 62 47 f9` | ldr x1,[x20, #0xec0] | `FALL_THROUGH`
<a id="insn-00bdf230"></a> `00bdf230` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdf234"></a> `00bdf234` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdf238"></a> `00bdf238` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdf23c"></a> `00bdf23c` | `9f 62 07 f9` | str xzr,[x20, #0xec0] | `FALL_THROUGH`
<a id="insn-00bdf240"></a> `00bdf240` | `54 2a 00 90` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdf244"></a> `00bdf244` | `81 76 47 f9` | ldr x1,[x20, #0xee8] | `FALL_THROUGH`
<a id="insn-00bdf248"></a> `00bdf248` | `21 02 00 b4` | cbz x1,0x00bdf28c | `CONDITIONAL_JUMP`
<a id="insn-00bdf24c"></a> `00bdf24c` | `55 2a 00 90` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdf250"></a> `00bdf250` | `a8 c2 7b 39` | ldrb w8,[x21, #0xef0] | `FALL_THROUGH`
<a id="insn-00bdf254"></a> `00bdf254` | `c8 00 00 34` | cbz w8,0x00bdf26c | `CONDITIONAL_JUMP`
<a id="insn-00bdf258"></a> `00bdf258` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdf25c"></a> `00bdf25c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdf260"></a> `00bdf260` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bdf264"></a> `00bdf264` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdf268"></a> `00bdf268` | `bf c2 3b 39` | strb wzr,[x21, #0xef0] | `FALL_THROUGH`
<a id="insn-00bdf26c"></a> `00bdf26c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdf270"></a> `00bdf270` | `64 f3 01 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf274"></a> `00bdf274` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdf278"></a> `00bdf278` | `81 76 47 f9` | ldr x1,[x20, #0xee8] | `FALL_THROUGH`
<a id="insn-00bdf27c"></a> `00bdf27c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdf280"></a> `00bdf280` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdf284"></a> `00bdf284` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdf288"></a> `00bdf288` | `9f 76 07 f9` | str xzr,[x20, #0xee8] | `FALL_THROUGH`
<a id="insn-00bdf28c"></a> `00bdf28c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdf290"></a> `00bdf290` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf294"></a> `00bdf294` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdf298"></a> `00bdf298` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdf0fc`](#insn-00bdf0fc) 範囲 `[['00bdf0fc', '00bdf11b']]`
  - `CONDITIONAL_JUMP` [`00bdf118`](#insn-00bdf118) → [`00bdf15c`](#insn-00bdf15c)
  - `FALL_THROUGH` [`00bdf118`](#insn-00bdf118) → [`00bdf11c`](#insn-00bdf11c)
- ブロック [`00bdf11c`](#insn-00bdf11c) 範囲 `[['00bdf11c', '00bdf127']]`
  - `CONDITIONAL_JUMP` [`00bdf124`](#insn-00bdf124) → [`00bdf13c`](#insn-00bdf13c)
  - `FALL_THROUGH` [`00bdf124`](#insn-00bdf124) → [`00bdf128`](#insn-00bdf128)
- ブロック [`00bdf128`](#insn-00bdf128) 範囲 `[['00bdf128', '00bdf13b']]`
  - `FALL_THROUGH` [`00bdf138`](#insn-00bdf138) → [`00bdf13c`](#insn-00bdf13c)
- ブロック [`00bdf13c`](#insn-00bdf13c) 範囲 `[['00bdf13c', '00bdf15b']]`
  - `FALL_THROUGH` [`00bdf158`](#insn-00bdf158) → [`00bdf15c`](#insn-00bdf15c)
- ブロック [`00bdf15c`](#insn-00bdf15c) 範囲 `[['00bdf15c', '00bdf167']]`
  - `CONDITIONAL_JUMP` [`00bdf164`](#insn-00bdf164) → [`00bdf1a8`](#insn-00bdf1a8)
  - `FALL_THROUGH` [`00bdf164`](#insn-00bdf164) → [`00bdf168`](#insn-00bdf168)
- ブロック [`00bdf168`](#insn-00bdf168) 範囲 `[['00bdf168', '00bdf173']]`
  - `CONDITIONAL_JUMP` [`00bdf170`](#insn-00bdf170) → [`00bdf188`](#insn-00bdf188)
  - `FALL_THROUGH` [`00bdf170`](#insn-00bdf170) → [`00bdf174`](#insn-00bdf174)
- ブロック [`00bdf174`](#insn-00bdf174) 範囲 `[['00bdf174', '00bdf187']]`
  - `FALL_THROUGH` [`00bdf184`](#insn-00bdf184) → [`00bdf188`](#insn-00bdf188)
- ブロック [`00bdf188`](#insn-00bdf188) 範囲 `[['00bdf188', '00bdf1a7']]`
  - `FALL_THROUGH` [`00bdf1a4`](#insn-00bdf1a4) → [`00bdf1a8`](#insn-00bdf1a8)
- ブロック [`00bdf1a8`](#insn-00bdf1a8) 範囲 `[['00bdf1a8', '00bdf1b3']]`
  - `CONDITIONAL_JUMP` [`00bdf1b0`](#insn-00bdf1b0) → [`00bdf1f4`](#insn-00bdf1f4)
  - `FALL_THROUGH` [`00bdf1b0`](#insn-00bdf1b0) → [`00bdf1b4`](#insn-00bdf1b4)
- ブロック [`00bdf1b4`](#insn-00bdf1b4) 範囲 `[['00bdf1b4', '00bdf1bf']]`
  - `CONDITIONAL_JUMP` [`00bdf1bc`](#insn-00bdf1bc) → [`00bdf1d4`](#insn-00bdf1d4)
  - `FALL_THROUGH` [`00bdf1bc`](#insn-00bdf1bc) → [`00bdf1c0`](#insn-00bdf1c0)
- ブロック [`00bdf1c0`](#insn-00bdf1c0) 範囲 `[['00bdf1c0', '00bdf1d3']]`
  - `FALL_THROUGH` [`00bdf1d0`](#insn-00bdf1d0) → [`00bdf1d4`](#insn-00bdf1d4)
- ブロック [`00bdf1d4`](#insn-00bdf1d4) 範囲 `[['00bdf1d4', '00bdf1f3']]`
  - `FALL_THROUGH` [`00bdf1f0`](#insn-00bdf1f0) → [`00bdf1f4`](#insn-00bdf1f4)
- ブロック [`00bdf1f4`](#insn-00bdf1f4) 範囲 `[['00bdf1f4', '00bdf1ff']]`
  - `CONDITIONAL_JUMP` [`00bdf1fc`](#insn-00bdf1fc) → [`00bdf240`](#insn-00bdf240)
  - `FALL_THROUGH` [`00bdf1fc`](#insn-00bdf1fc) → [`00bdf200`](#insn-00bdf200)
- ブロック [`00bdf200`](#insn-00bdf200) 範囲 `[['00bdf200', '00bdf20b']]`
  - `CONDITIONAL_JUMP` [`00bdf208`](#insn-00bdf208) → [`00bdf220`](#insn-00bdf220)
  - `FALL_THROUGH` [`00bdf208`](#insn-00bdf208) → [`00bdf20c`](#insn-00bdf20c)
- ブロック [`00bdf20c`](#insn-00bdf20c) 範囲 `[['00bdf20c', '00bdf21f']]`
  - `FALL_THROUGH` [`00bdf21c`](#insn-00bdf21c) → [`00bdf220`](#insn-00bdf220)
- ブロック [`00bdf220`](#insn-00bdf220) 範囲 `[['00bdf220', '00bdf23f']]`
  - `FALL_THROUGH` [`00bdf23c`](#insn-00bdf23c) → [`00bdf240`](#insn-00bdf240)
- ブロック [`00bdf240`](#insn-00bdf240) 範囲 `[['00bdf240', '00bdf24b']]`
  - `CONDITIONAL_JUMP` [`00bdf248`](#insn-00bdf248) → [`00bdf28c`](#insn-00bdf28c)
  - `FALL_THROUGH` [`00bdf248`](#insn-00bdf248) → [`00bdf24c`](#insn-00bdf24c)
- ブロック [`00bdf24c`](#insn-00bdf24c) 範囲 `[['00bdf24c', '00bdf257']]`
  - `CONDITIONAL_JUMP` [`00bdf254`](#insn-00bdf254) → [`00bdf26c`](#insn-00bdf26c)
  - `FALL_THROUGH` [`00bdf254`](#insn-00bdf254) → [`00bdf258`](#insn-00bdf258)
- ブロック [`00bdf258`](#insn-00bdf258) 範囲 `[['00bdf258', '00bdf26b']]`
  - `FALL_THROUGH` [`00bdf268`](#insn-00bdf268) → [`00bdf26c`](#insn-00bdf26c)
- ブロック [`00bdf26c`](#insn-00bdf26c) 範囲 `[['00bdf26c', '00bdf28b']]`
  - `FALL_THROUGH` [`00bdf288`](#insn-00bdf288) → [`00bdf28c`](#insn-00bdf28c)
- ブロック [`00bdf28c`](#insn-00bdf28c) 範囲 `[['00bdf28c', '00bdf29b']]`

## 命令位置別の参照

- [`00bdf0fc`](#insn-00bdf0fc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf100`](#insn-00bdf100) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf104`](#insn-00bdf104) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf110`](#insn-00bdf110) → `01127dc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf118`](#insn-00bdf118) → [`00bdf15c`](#insn-00bdf15c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf120`](#insn-00bdf120) → `01127dc8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdf124`](#insn-00bdf124) → [`00bdf13c`](#insn-00bdf13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf138`](#insn-00bdf138) → `01127dc8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdf140`](#insn-00bdf140) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bdf148`](#insn-00bdf148) → `01127dc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf158`](#insn-00bdf158) → `01127dc0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf160`](#insn-00bdf160) → `01127de0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf164`](#insn-00bdf164) → [`00bdf1a8`](#insn-00bdf1a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf16c`](#insn-00bdf16c) → `01127de8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdf170`](#insn-00bdf170) → [`00bdf188`](#insn-00bdf188) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf184`](#insn-00bdf184) → `01127de8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdf18c`](#insn-00bdf18c) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bdf194`](#insn-00bdf194) → `01127de0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf1a4`](#insn-00bdf1a4) → `01127de0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf1ac`](#insn-00bdf1ac) → `01127e70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf1b0`](#insn-00bdf1b0) → [`00bdf1f4`](#insn-00bdf1f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf1b8`](#insn-00bdf1b8) → `01127e78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdf1bc`](#insn-00bdf1bc) → [`00bdf1d4`](#insn-00bdf1d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf1d0`](#insn-00bdf1d0) → `01127e78`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdf1d8`](#insn-00bdf1d8) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bdf1e0`](#insn-00bdf1e0) → `01127e70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf1f0`](#insn-00bdf1f0) → `01127e70`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf1f8`](#insn-00bdf1f8) → `01127ec0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf1fc`](#insn-00bdf1fc) → [`00bdf240`](#insn-00bdf240) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf204`](#insn-00bdf204) → `01127ec8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdf208`](#insn-00bdf208) → [`00bdf220`](#insn-00bdf220) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf21c`](#insn-00bdf21c) → `01127ec8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdf224`](#insn-00bdf224) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bdf22c`](#insn-00bdf22c) → `01127ec0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf23c`](#insn-00bdf23c) → `01127ec0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf244`](#insn-00bdf244) → `01127ee8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf248`](#insn-00bdf248) → [`00bdf28c`](#insn-00bdf28c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf250`](#insn-00bdf250) → `01127ef0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdf254`](#insn-00bdf254) → [`00bdf26c`](#insn-00bdf26c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf268`](#insn-00bdf268) → `01127ef0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdf270`](#insn-00bdf270) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bdf278`](#insn-00bdf278) → `01127ee8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf288`](#insn-00bdf288) → `01127ee8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf28c`](#insn-00bdf28c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf290`](#insn-00bdf290) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdf0fc`](#insn-00bdf0fc)

~~~json
{
  "source": "00bdf0fc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf100`](#insn-00bdf100)

~~~json
{
  "source": "00bdf100",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf104`](#insn-00bdf104)

~~~json
{
  "source": "00bdf104",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf110`](#insn-00bdf110)

~~~json
{
  "source": "00bdf110",
  "target": "01127dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127dc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf118`](#insn-00bdf118)

~~~json
{
  "source": "00bdf118",
  "target": "00bdf15c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf120`](#insn-00bdf120)

~~~json
{
  "source": "00bdf120",
  "target": "01127dc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127dc8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf124`](#insn-00bdf124)

~~~json
{
  "source": "00bdf124",
  "target": "00bdf13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf138`](#insn-00bdf138)

~~~json
{
  "source": "00bdf138",
  "target": "01127dc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127dc8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf140`](#insn-00bdf140)

~~~json
{
  "source": "00bdf140",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf148`](#insn-00bdf148)

~~~json
{
  "source": "00bdf148",
  "target": "01127dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127dc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf158`](#insn-00bdf158)

~~~json
{
  "source": "00bdf158",
  "target": "01127dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127dc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf160`](#insn-00bdf160)

~~~json
{
  "source": "00bdf160",
  "target": "01127de0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127de0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf164`](#insn-00bdf164)

~~~json
{
  "source": "00bdf164",
  "target": "00bdf1a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf16c`](#insn-00bdf16c)

~~~json
{
  "source": "00bdf16c",
  "target": "01127de8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127de8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf170`](#insn-00bdf170)

~~~json
{
  "source": "00bdf170",
  "target": "00bdf188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf184`](#insn-00bdf184)

~~~json
{
  "source": "00bdf184",
  "target": "01127de8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127de8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf18c`](#insn-00bdf18c)

~~~json
{
  "source": "00bdf18c",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf194`](#insn-00bdf194)

~~~json
{
  "source": "00bdf194",
  "target": "01127de0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127de0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf1a4`](#insn-00bdf1a4)

~~~json
{
  "source": "00bdf1a4",
  "target": "01127de0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127de0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf1ac`](#insn-00bdf1ac)

~~~json
{
  "source": "00bdf1ac",
  "target": "01127e70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127e70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf1b0`](#insn-00bdf1b0)

~~~json
{
  "source": "00bdf1b0",
  "target": "00bdf1f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf1b8`](#insn-00bdf1b8)

~~~json
{
  "source": "00bdf1b8",
  "target": "01127e78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127e78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf1bc`](#insn-00bdf1bc)

~~~json
{
  "source": "00bdf1bc",
  "target": "00bdf1d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf1d0`](#insn-00bdf1d0)

~~~json
{
  "source": "00bdf1d0",
  "target": "01127e78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127e78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf1d8`](#insn-00bdf1d8)

~~~json
{
  "source": "00bdf1d8",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf1e0`](#insn-00bdf1e0)

~~~json
{
  "source": "00bdf1e0",
  "target": "01127e70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127e70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf1f0`](#insn-00bdf1f0)

~~~json
{
  "source": "00bdf1f0",
  "target": "01127e70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127e70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf1f8`](#insn-00bdf1f8)

~~~json
{
  "source": "00bdf1f8",
  "target": "01127ec0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ec0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf1fc`](#insn-00bdf1fc)

~~~json
{
  "source": "00bdf1fc",
  "target": "00bdf240",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf204`](#insn-00bdf204)

~~~json
{
  "source": "00bdf204",
  "target": "01127ec8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ec8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf208`](#insn-00bdf208)

~~~json
{
  "source": "00bdf208",
  "target": "00bdf220",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf21c`](#insn-00bdf21c)

~~~json
{
  "source": "00bdf21c",
  "target": "01127ec8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ec8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf224`](#insn-00bdf224)

~~~json
{
  "source": "00bdf224",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf22c`](#insn-00bdf22c)

~~~json
{
  "source": "00bdf22c",
  "target": "01127ec0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ec0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf23c`](#insn-00bdf23c)

~~~json
{
  "source": "00bdf23c",
  "target": "01127ec0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ec0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf244`](#insn-00bdf244)

~~~json
{
  "source": "00bdf244",
  "target": "01127ee8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ee8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf248`](#insn-00bdf248)

~~~json
{
  "source": "00bdf248",
  "target": "00bdf28c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf250`](#insn-00bdf250)

~~~json
{
  "source": "00bdf250",
  "target": "01127ef0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ef0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf254`](#insn-00bdf254)

~~~json
{
  "source": "00bdf254",
  "target": "00bdf26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf268`](#insn-00bdf268)

~~~json
{
  "source": "00bdf268",
  "target": "01127ef0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ef0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf270`](#insn-00bdf270)

~~~json
{
  "source": "00bdf270",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf278`](#insn-00bdf278)

~~~json
{
  "source": "00bdf278",
  "target": "01127ee8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ee8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf288`](#insn-00bdf288)

~~~json
{
  "source": "00bdf288",
  "target": "01127ee8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ee8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf28c`](#insn-00bdf28c)

~~~json
{
  "source": "00bdf28c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf290`](#insn-00bdf290)

~~~json
{
  "source": "00bdf290",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
