# 00aca2ac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aca268`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca268.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-241a7068feed00d264b2287025858412)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b29d3c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29d3c.md) · 移動量 `+0x5fa90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0018.md#compare-b199e2c03f42cb328deb3c94a3310e0b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aca2ac",
  "name": "FUN_00aca2ac",
  "size": 404,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8f9e8d6884709900551428ed8f2f4f18bf0da64125df18bf99a90a84a912e2b0",
  "source_text_sha256": "8f9e8d6884709900551428ed8f2f4f18bf0da64125df18bf99a90a84a912e2b0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aca2ac",
        "00aca43f"
      ]
    ],
    "bytes_sha256": "3b738fcd52b6018b5a700105bc11f27a468392498b30c36705ac50f39a73ad3a",
    "instruction_count": 101,
    "instruction_bytes": 404,
    "body_bytes": 404,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ab3444](../00ab3/00ab3444.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [00aca440](../00aca/00aca440.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb1b0](../00bdb/00bdb1b0.md)
- [00bdb240](../00bdb/00bdb240.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1626 bytes

~~~c

void FUN_00aca2ac(undefined8 *param_1,ulong param_2)

{
  ulong uVar1;
  long lVar2;
  ulong uVar3;
  void *__src;
  size_t sVar4;
  void *pvVar5;
  size_t __n;
  
  pvVar5 = (void *)param_1[1];
  if ((ulong)((param_1[2] - (long)pvVar5 >> 7) * -0x5555555555555555) < param_2) {
    __src = (void *)*param_1;
    sVar4 = (long)pvVar5 - (long)__src;
    uVar1 = ((long)sVar4 >> 7) * -0x5555555555555555 + param_2;
    if (0xaaaaaaaaaaaaaa < uVar1) {
      FUN_00aca440(param_1);
LAB_00aca43c:
                    /* WARNING: Subroutine does not return */
      FUN_0041e380();
    }
    lVar2 = param_1[2] - (long)__src >> 7;
    uVar3 = lVar2 * 0x5555555555555556;
    if (uVar3 < uVar1 || uVar3 - uVar1 == 0) {
      uVar3 = uVar1;
    }
    if (0x55555555555554 < (ulong)(lVar2 * -0x5555555555555555)) {
      uVar3 = 0xaaaaaaaaaaaaaa;
    }
    if (uVar3 == 0) {
      lVar2 = 0;
    }
    else {
      if (0xaaaaaaaaaaaaaa < uVar3) goto LAB_00aca43c;
      lVar2 = _Znwm(uVar3 * 0x180);
    }
    pvVar5 = (void *)(lVar2 + ((long)sVar4 >> 7) * 0x80);
    __n = ((param_2 * 0x180 - 0x180) / 0x180) * 0x180 + 0x180;
    memset(pvVar5,0,__n);
    memcpy((void *)((long)pvVar5 - sVar4),__src,sVar4);
    *param_1 = (void *)((long)pvVar5 - sVar4);
    param_1[1] = (long)pvVar5 + __n;
    param_1[2] = lVar2 + uVar3 * 0x180;
    if (__src != (void *)0x0) {
      _ZdlPv(__src);
      return;
    }
  }
  else {
    if (param_2 != 0) {
      sVar4 = ((param_2 * 0x180 - 0x180) / 0x180) * 0x180 + 0x180;
      memset(pvVar5,0,sVar4);
      pvVar5 = (void *)((long)pvVar5 + sVar4);
    }
    param_1[1] = pvVar5;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aca2ac"></a> `00aca2ac` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00aca2b0"></a> `00aca2b0` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aca2b4"></a> `00aca2b4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aca2b8"></a> `00aca2b8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aca2bc"></a> `00aca2bc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aca2c0"></a> `00aca2c0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aca2c4"></a> `00aca2c4` | `15 a0 40 a9` | ldp x21,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aca2c8"></a> `00aca2c8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aca2cc"></a> `00aca2cc` | `09 01 15 cb` | sub x9,x8,x21 | `FALL_THROUGH`
<a id="insn-00aca2d0"></a> `00aca2d0` | `2a fd 47 93` | asr x10,x9,#0x7 | `FALL_THROUGH`
<a id="insn-00aca2d4"></a> `00aca2d4` | `e9 f3 01 b2` | orr x9,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00aca2d8"></a> `00aca2d8` | `69 55 95 f2` | movk x9,#0xaaab | `FALL_THROUGH`
<a id="insn-00aca2dc"></a> `00aca2dc` | `4a 7d 09 9b` | mul x10,x10,x9 | `FALL_THROUGH`
<a id="insn-00aca2e0"></a> `00aca2e0` | `5f 01 01 eb` | cmp x10,x1 | `FALL_THROUGH`
<a id="insn-00aca2e4"></a> `00aca2e4` | `e2 03 00 54` | b.cs 0x00aca360 | `CONDITIONAL_JUMP`
<a id="insn-00aca2e8"></a> `00aca2e8` | `74 02 40 f9` | ldr x20,[x19] | `FALL_THROUGH`
<a id="insn-00aca2ec"></a> `00aca2ec` | `b5 02 14 cb` | sub x21,x21,x20 | `FALL_THROUGH`
<a id="insn-00aca2f0"></a> `00aca2f0` | `aa fe 47 93` | asr x10,x21,#0x7 | `FALL_THROUGH`
<a id="insn-00aca2f4"></a> `00aca2f4` | `56 7d 09 9b` | mul x22,x10,x9 | `FALL_THROUGH`
<a id="insn-00aca2f8"></a> `00aca2f8` | `e9 f3 01 b2` | orr x9,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00aca2fc"></a> `00aca2fc` | `49 15 e0 f2` | movk x9,#0xaa, LSL #48 | `FALL_THROUGH`
<a id="insn-00aca300"></a> `00aca300` | `ca 02 01 8b` | add x10,x22,x1 | `FALL_THROUGH`
<a id="insn-00aca304"></a> `00aca304` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00aca308"></a> `00aca308` | `68 09 00 54` | b.hi 0x00aca434 | `CONDITIONAL_JUMP`
<a id="insn-00aca30c"></a> `00aca30c` | `08 01 14 cb` | sub x8,x8,x20 | `FALL_THROUGH`
<a id="insn-00aca310"></a> `00aca310` | `f7 f3 01 b2` | orr x23,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00aca314"></a> `00aca314` | `ec f3 00 b2` | orr x12,xzr,#0x5555555555555555 | `FALL_THROUGH`
<a id="insn-00aca318"></a> `00aca318` | `08 fd 47 93` | asr x8,x8,#0x7 | `FALL_THROUGH`
<a id="insn-00aca31c"></a> `00aca31c` | `77 55 95 f2` | movk x23,#0xaaab | `FALL_THROUGH`
<a id="insn-00aca320"></a> `00aca320` | `ac 0a e0 f2` | movk x12,#0x55, LSL #48 | `FALL_THROUGH`
<a id="insn-00aca324"></a> `00aca324` | `08 7d 17 9b` | mul x8,x8,x23 | `FALL_THROUGH`
<a id="insn-00aca328"></a> `00aca328` | `0b f9 7f d3` | lsl x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aca32c"></a> `00aca32c` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00aca330"></a> `00aca330` | `6a 81 8a 9a` | csel x10,x11,x10,hi | `FALL_THROUGH`
<a id="insn-00aca334"></a> `00aca334` | `1f 01 0c eb` | cmp x8,x12 | `FALL_THROUGH`
<a id="insn-00aca338"></a> `00aca338` | `58 31 89 9a` | csel x24,x10,x9,cc | `FALL_THROUGH`
<a id="insn-00aca33c"></a> `00aca33c` | `58 03 00 b4` | cbz x24,0x00aca3a4 | `CONDITIONAL_JUMP`
<a id="insn-00aca340"></a> `00aca340` | `1f 03 09 eb` | cmp x24,x9 | `FALL_THROUGH`
<a id="insn-00aca344"></a> `00aca344` | `c8 07 00 54` | b.hi 0x00aca43c | `CONDITIONAL_JUMP`
<a id="insn-00aca348"></a> `00aca348` | `08 07 18 8b` | add x8,x24,x24, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00aca34c"></a> `00aca34c` | `f9 03 01 aa` | mov x25,x1 | `FALL_THROUGH`
<a id="insn-00aca350"></a> `00aca350` | `00 e1 79 d3` | lsl x0,x8,#0x7 | `FALL_THROUGH`
<a id="insn-00aca354"></a> `00aca354` | `3b 43 04 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00aca358"></a> `00aca358` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00aca35c"></a> `00aca35c` | `13 00 00 14` | b 0x00aca3a8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aca360"></a> `00aca360` | `e1 01 00 b4` | cbz x1,0x00aca39c | `CONDITIONAL_JUMP`
<a id="insn-00aca364"></a> `00aca364` | `08 30 80 52` | mov w8,#0x180 | `FALL_THROUGH`
<a id="insn-00aca368"></a> `00aca368` | `e9 2f 80 92` | mov x9,#-0x180 | `FALL_THROUGH`
<a id="insn-00aca36c"></a> `00aca36c` | `ea f3 01 b2` | orr x10,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00aca370"></a> `00aca370` | `29 24 08 9b` | madd x9,x1,x8,x9 | `FALL_THROUGH`
<a id="insn-00aca374"></a> `00aca374` | `6a 55 95 f2` | movk x10,#0xaaab | `FALL_THROUGH`
<a id="insn-00aca378"></a> `00aca378` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aca37c"></a> `00aca37c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aca380"></a> `00aca380` | `29 7d ca 9b` | umulh x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00aca384"></a> `00aca384` | `0a 30 80 d2` | mov x10,#0x180 | `FALL_THROUGH`
<a id="insn-00aca388"></a> `00aca388` | `29 fd 48 d3` | lsr x9,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00aca38c"></a> `00aca38c` | `34 29 08 9b` | madd x20,x9,x8,x10 | `FALL_THROUGH`
<a id="insn-00aca390"></a> `00aca390` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00aca394"></a> `00aca394` | `ab 43 04 94` | bl 0x00bdb240 | `UNCONDITIONAL_CALL`
<a id="insn-00aca398"></a> `00aca398` | `b5 02 14 8b` | add x21,x21,x20 | `FALL_THROUGH`
<a id="insn-00aca39c"></a> `00aca39c` | `75 06 00 f9` | str x21,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aca3a0"></a> `00aca3a0` | `1f 00 00 14` | b 0x00aca41c | `UNCONDITIONAL_JUMP`
<a id="insn-00aca3a4"></a> `00aca3a4` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00aca3a8"></a> `00aca3a8` | `08 30 80 52` | mov w8,#0x180 | `FALL_THROUGH`
<a id="insn-00aca3ac"></a> `00aca3ac` | `e9 2f 80 92` | mov x9,#-0x180 | `FALL_THROUGH`
<a id="insn-00aca3b0"></a> `00aca3b0` | `0a 30 80 d2` | mov x10,#0x180 | `FALL_THROUGH`
<a id="insn-00aca3b4"></a> `00aca3b4` | `29 24 08 9b` | madd x9,x1,x8,x9 | `FALL_THROUGH`
<a id="insn-00aca3b8"></a> `00aca3b8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aca3bc"></a> `00aca3bc` | `d6 02 08 9b` | madd x22,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00aca3c0"></a> `00aca3c0` | `18 03 08 9b` | madd x24,x24,x8,x0 | `FALL_THROUGH`
<a id="insn-00aca3c4"></a> `00aca3c4` | `29 7d d7 9b` | umulh x9,x9,x23 | `FALL_THROUGH`
<a id="insn-00aca3c8"></a> `00aca3c8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00aca3cc"></a> `00aca3cc` | `29 fd 48 d3` | lsr x9,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00aca3d0"></a> `00aca3d0` | `37 29 08 9b` | madd x23,x9,x8,x10 | `FALL_THROUGH`
<a id="insn-00aca3d4"></a> `00aca3d4` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00aca3d8"></a> `00aca3d8` | `9a 43 04 94` | bl 0x00bdb240 | `UNCONDITIONAL_CALL`
<a id="insn-00aca3dc"></a> `00aca3dc` | `d7 02 17 8b` | add x23,x22,x23 | `FALL_THROUGH`
<a id="insn-00aca3e0"></a> `00aca3e0` | `d6 02 15 cb` | sub x22,x22,x21 | `FALL_THROUGH`
<a id="insn-00aca3e4"></a> `00aca3e4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00aca3e8"></a> `00aca3e8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00aca3ec"></a> `00aca3ec` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00aca3f0"></a> `00aca3f0` | `70 43 04 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00aca3f4"></a> `00aca3f4` | `76 5e 00 a9` | stp x22,x23,[x19] | `FALL_THROUGH`
<a id="insn-00aca3f8"></a> `00aca3f8` | `78 0a 00 f9` | str x24,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aca3fc"></a> `00aca3fc` | `14 01 00 b4` | cbz x20,0x00aca41c | `CONDITIONAL_JUMP`
<a id="insn-00aca400"></a> `00aca400` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aca404"></a> `00aca404` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aca408"></a> `00aca408` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aca40c"></a> `00aca40c` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aca410"></a> `00aca410` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aca414"></a> `00aca414` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00aca418"></a> `00aca418` | `12 43 04 14` | b 0x00bdb060 | `CALL_TERMINATOR`
<a id="insn-00aca41c"></a> `00aca41c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aca420"></a> `00aca420` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aca424"></a> `00aca424` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aca428"></a> `00aca428` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aca42c"></a> `00aca42c` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00aca430"></a> `00aca430` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aca434"></a> `00aca434` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aca438"></a> `00aca438` | `02 00 00 94` | bl 0x00aca440 | `UNCONDITIONAL_CALL`
<a id="insn-00aca43c"></a> `00aca43c` | `d1 4f e5 97` | bl 0x0041e380 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aca2ac`](#insn-00aca2ac) 範囲 `[['00aca2ac', '00aca2e7']]`
  - `CONDITIONAL_JUMP` [`00aca2e4`](#insn-00aca2e4) → [`00aca360`](#insn-00aca360)
  - `FALL_THROUGH` [`00aca2e4`](#insn-00aca2e4) → [`00aca2e8`](#insn-00aca2e8)
- ブロック [`00aca2e8`](#insn-00aca2e8) 範囲 `[['00aca2e8', '00aca30b']]`
  - `CONDITIONAL_JUMP` [`00aca308`](#insn-00aca308) → [`00aca434`](#insn-00aca434)
  - `FALL_THROUGH` [`00aca308`](#insn-00aca308) → [`00aca30c`](#insn-00aca30c)
- ブロック [`00aca30c`](#insn-00aca30c) 範囲 `[['00aca30c', '00aca33f']]`
  - `CONDITIONAL_JUMP` [`00aca33c`](#insn-00aca33c) → [`00aca3a4`](#insn-00aca3a4)
  - `FALL_THROUGH` [`00aca33c`](#insn-00aca33c) → [`00aca340`](#insn-00aca340)
- ブロック [`00aca340`](#insn-00aca340) 範囲 `[['00aca340', '00aca347']]`
  - `CONDITIONAL_JUMP` [`00aca344`](#insn-00aca344) → [`00aca43c`](#insn-00aca43c)
  - `FALL_THROUGH` [`00aca344`](#insn-00aca344) → [`00aca348`](#insn-00aca348)
- ブロック [`00aca348`](#insn-00aca348) 範囲 `[['00aca348', '00aca35f']]`
  - `UNCONDITIONAL_JUMP` [`00aca35c`](#insn-00aca35c) → [`00aca3a8`](#insn-00aca3a8)
- ブロック [`00aca360`](#insn-00aca360) 範囲 `[['00aca360', '00aca363']]`
  - `CONDITIONAL_JUMP` [`00aca360`](#insn-00aca360) → [`00aca39c`](#insn-00aca39c)
  - `FALL_THROUGH` [`00aca360`](#insn-00aca360) → [`00aca364`](#insn-00aca364)
- ブロック [`00aca364`](#insn-00aca364) 範囲 `[['00aca364', '00aca39b']]`
  - `FALL_THROUGH` [`00aca398`](#insn-00aca398) → [`00aca39c`](#insn-00aca39c)
- ブロック [`00aca39c`](#insn-00aca39c) 範囲 `[['00aca39c', '00aca3a3']]`
  - `UNCONDITIONAL_JUMP` [`00aca3a0`](#insn-00aca3a0) → [`00aca41c`](#insn-00aca41c)
- ブロック [`00aca3a4`](#insn-00aca3a4) 範囲 `[['00aca3a4', '00aca3a7']]`
  - `FALL_THROUGH` [`00aca3a4`](#insn-00aca3a4) → [`00aca3a8`](#insn-00aca3a8)
- ブロック [`00aca3a8`](#insn-00aca3a8) 範囲 `[['00aca3a8', '00aca3ff']]`
  - `CONDITIONAL_JUMP` [`00aca3fc`](#insn-00aca3fc) → [`00aca41c`](#insn-00aca41c)
  - `FALL_THROUGH` [`00aca3fc`](#insn-00aca3fc) → [`00aca400`](#insn-00aca400)
- ブロック [`00aca400`](#insn-00aca400) 範囲 `[['00aca400', '00aca41b']]`
- ブロック [`00aca41c`](#insn-00aca41c) 範囲 `[['00aca41c', '00aca433']]`
- ブロック [`00aca434`](#insn-00aca434) 範囲 `[['00aca434', '00aca43b']]`
  - `FALL_THROUGH` [`00aca438`](#insn-00aca438) → [`00aca43c`](#insn-00aca43c)
- ブロック [`00aca43c`](#insn-00aca43c) 範囲 `[['00aca43c', '00aca43f']]`

## 命令位置別の参照

- [`00aca2ac`](#insn-00aca2ac) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca2b0`](#insn-00aca2b0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca2b4`](#insn-00aca2b4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca2b8`](#insn-00aca2b8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca2bc`](#insn-00aca2bc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca2e4`](#insn-00aca2e4) → [`00aca360`](#insn-00aca360) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca308`](#insn-00aca308) → [`00aca434`](#insn-00aca434) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca33c`](#insn-00aca33c) → [`00aca3a4`](#insn-00aca3a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca344`](#insn-00aca344) → [`00aca43c`](#insn-00aca43c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca354`](#insn-00aca354) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00aca35c`](#insn-00aca35c) → [`00aca3a8`](#insn-00aca3a8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca360`](#insn-00aca360) → [`00aca39c`](#insn-00aca39c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca394`](#insn-00aca394) → [`00bdb240`](../00bdb/00bdb240.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb240` · 推定シンボル `None` · 推定型 `None`
- [`00aca3a0`](#insn-00aca3a0) → [`00aca41c`](#insn-00aca41c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca3d8`](#insn-00aca3d8) → [`00bdb240`](../00bdb/00bdb240.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb240` · 推定シンボル `None` · 推定型 `None`
- [`00aca3f0`](#insn-00aca3f0) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00aca3fc`](#insn-00aca3fc) → [`00aca41c`](#insn-00aca41c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca404`](#insn-00aca404) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca408`](#insn-00aca408) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca40c`](#insn-00aca40c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca410`](#insn-00aca410) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca414`](#insn-00aca414) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca418`](#insn-00aca418) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aca41c`](#insn-00aca41c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca420`](#insn-00aca420) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca424`](#insn-00aca424) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca428`](#insn-00aca428) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca42c`](#insn-00aca42c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca438`](#insn-00aca438) → [`00aca440`](00aca440.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aca440` · 推定シンボル `None` · 推定型 `None`
- [`00aca43c`](#insn-00aca43c) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aca2ac`](#insn-00aca2ac)

~~~json
{
  "source": "00aca2ac",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca2b0`](#insn-00aca2b0)

~~~json
{
  "source": "00aca2b0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca2b4`](#insn-00aca2b4)

~~~json
{
  "source": "00aca2b4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca2b8`](#insn-00aca2b8)

~~~json
{
  "source": "00aca2b8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca2bc`](#insn-00aca2bc)

~~~json
{
  "source": "00aca2bc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca2e4`](#insn-00aca2e4)

~~~json
{
  "source": "00aca2e4",
  "target": "00aca360",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca308`](#insn-00aca308)

~~~json
{
  "source": "00aca308",
  "target": "00aca434",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca33c`](#insn-00aca33c)

~~~json
{
  "source": "00aca33c",
  "target": "00aca3a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca344`](#insn-00aca344)

~~~json
{
  "source": "00aca344",
  "target": "00aca43c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca354`](#insn-00aca354)

~~~json
{
  "source": "00aca354",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca35c`](#insn-00aca35c)

~~~json
{
  "source": "00aca35c",
  "target": "00aca3a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca360`](#insn-00aca360)

~~~json
{
  "source": "00aca360",
  "target": "00aca39c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca394`](#insn-00aca394)

~~~json
{
  "source": "00aca394",
  "target": "00bdb240",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca3a0`](#insn-00aca3a0)

~~~json
{
  "source": "00aca3a0",
  "target": "00aca41c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca3d8`](#insn-00aca3d8)

~~~json
{
  "source": "00aca3d8",
  "target": "00bdb240",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca3f0`](#insn-00aca3f0)

~~~json
{
  "source": "00aca3f0",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca3fc`](#insn-00aca3fc)

~~~json
{
  "source": "00aca3fc",
  "target": "00aca41c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca404`](#insn-00aca404)

~~~json
{
  "source": "00aca404",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca408`](#insn-00aca408)

~~~json
{
  "source": "00aca408",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca40c`](#insn-00aca40c)

~~~json
{
  "source": "00aca40c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca410`](#insn-00aca410)

~~~json
{
  "source": "00aca410",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca414`](#insn-00aca414)

~~~json
{
  "source": "00aca414",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca418`](#insn-00aca418)

~~~json
{
  "source": "00aca418",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca41c`](#insn-00aca41c)

~~~json
{
  "source": "00aca41c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca420`](#insn-00aca420)

~~~json
{
  "source": "00aca420",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca424`](#insn-00aca424)

~~~json
{
  "source": "00aca424",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca428`](#insn-00aca428)

~~~json
{
  "source": "00aca428",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca42c`](#insn-00aca42c)

~~~json
{
  "source": "00aca42c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca438`](#insn-00aca438)

~~~json
{
  "source": "00aca438",
  "target": "00aca440",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca43c`](#insn-00aca43c)

~~~json
{
  "source": "00aca43c",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
