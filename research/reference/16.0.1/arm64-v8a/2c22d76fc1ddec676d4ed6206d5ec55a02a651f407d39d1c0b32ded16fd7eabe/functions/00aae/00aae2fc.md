# 00aae2fc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aae100`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aae/00aae100.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-c872d6c7757f9f7d026e481d5a632941)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aae36c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aae/00aae36c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0064.md#compare-58b66d5d290a6ccdb232f924ee4ab42d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aae2fc",
  "name": "FUN_00aae2fc",
  "size": 424,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cfcce6eb5e4d302d7b7ca5490f187d54db72c75c911cbc87f7b96f448dca72af",
  "source_text_sha256": "cfcce6eb5e4d302d7b7ca5490f187d54db72c75c911cbc87f7b96f448dca72af",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aae2fc",
        "00aae4a3"
      ]
    ],
    "bytes_sha256": "68f2b57e63b2b98734179f4e22e7b64d4c23f245440d5dfde12ede197e1575a3",
    "instruction_count": 106,
    "instruction_bytes": 424,
    "body_bytes": 424,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aae1cc](../00aae/00aae1cc.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3488 bytes

~~~c

long * FUN_00aae2fc(undefined8 *param_1,long *param_2,long *param_3,long *param_4,int *param_5)

{
  int iVar1;
  bool bVar2;
  long *plVar3;
  long *plVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  
  plVar4 = param_1 + 1;
  if (plVar4 != param_2) {
    iVar1 = *param_5;
    if ((int)param_2[4] <= iVar1) {
      if (iVar1 <= (int)param_2[4]) {
        *param_3 = (long)param_2;
        *param_4 = (long)param_2;
        return param_4;
      }
      plVar6 = (long *)param_2[1];
      plVar7 = param_2;
      plVar5 = plVar6;
      if (plVar6 == (long *)0x0) {
        do {
          plVar3 = (long *)plVar7[2];
          bVar2 = (long *)*plVar3 != plVar7;
          plVar7 = plVar3;
        } while (bVar2);
      }
      else {
        do {
          plVar3 = plVar5;
                    /* try { // try from 00aae360 to 00bae37b has its CatchHandler @ 00aae8dc */
          plVar5 = (long *)*plVar3;
        } while ((long *)*plVar3 != (long *)0x0);
      }
                    /* try { // try from 00aae428 to 00bae44b has its CatchHandler @ 00aae7c4 */
      if ((plVar3 == plVar4) || (iVar1 < (int)plVar3[4])) {
        if (plVar6 != (long *)0x0) {
          *param_3 = (long)plVar3;
          return plVar3;
        }
        *param_3 = (long)param_2;
        return param_2 + 1;
      }
                    /* try { // try from 00aae44c to 00bae467 has its CatchHandler @ 00aae26c */
      plVar5 = (long *)*plVar4;
      plVar7 = plVar4;
      while (plVar5 != (long *)0x0) {
                    /* try { // try from 00aae468 to 00bae46f has its CatchHandler @ 00aae87c */
        while (plVar7 = plVar5, iVar1 < (int)plVar7[4]) {
          plVar4 = plVar7;
          plVar5 = (long *)*plVar7;
          if ((long *)*plVar7 == (long *)0x0) goto LAB_00aae48c;
        }
        if (iVar1 <= (int)plVar7[4]) break;
        plVar4 = plVar7 + 1;
        plVar5 = (long *)*plVar4;
      }
LAB_00aae48c:
      *param_3 = (long)plVar7;
      return plVar4;
    }
  }
  plVar5 = (long *)*param_2;
  plVar7 = param_2;
  if ((long *)*param_1 != param_2) {
    plVar6 = param_2;
    plVar3 = plVar5;
    if (plVar5 == (long *)0x0) {
      do {
        plVar7 = (long *)plVar6[2];
        bVar2 = (long *)*plVar7 == plVar6;
        plVar6 = plVar7;
      } while (bVar2);
    }
    else {
      do {
                    /* try { // try from 00aae330 to 00bae35f has its CatchHandler @ 00aae26c */
        plVar7 = plVar3;
        plVar3 = (long *)plVar7[1];
      } while ((long *)plVar7[1] != (long *)0x0);
    }
    iVar1 = *param_5;
                    /* try { // try from 00aae390 to 00bae39b has its CatchHandler @ 00aae7d4 */
    if (iVar1 <= (int)plVar7[4]) {
      plVar5 = (long *)*plVar4;
      plVar7 = plVar4;
      while (plVar5 != (long *)0x0) {
                    /* try { // try from 00aae3d0 to 00bae3f7 has its CatchHandler @ 00aae7cc */
        while (plVar7 = plVar5, iVar1 < (int)plVar7[4]) {
          plVar4 = plVar7;
          plVar5 = (long *)*plVar7;
          if ((long *)*plVar7 == (long *)0x0) goto LAB_00aae3e8;
        }
        if (iVar1 <= (int)plVar7[4]) break;
        plVar4 = plVar7 + 1;
        plVar5 = (long *)*plVar4;
      }
LAB_00aae3e8:
      *param_3 = (long)plVar7;
      return plVar4;
    }
  }
  if (plVar5 != (long *)0x0) {
                    /* try { // try from 00aae39c to 00bae3cf has its CatchHandler @ 00aae26c */
    *param_3 = (long)plVar7;
    return plVar7 + 1;
  }
  *param_3 = (long)param_2;
  return param_2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aae2fc"></a> `00aae2fc` | `08 20 00 91` | add x8,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00aae300"></a> `00aae300` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00aae304"></a> `00aae304` | `a0 00 00 54` | b.eq 0x00aae318 | `CONDITIONAL_JUMP`
<a id="insn-00aae308"></a> `00aae308` | `89 00 40 b9` | ldr w9,[x4] | `FALL_THROUGH`
<a id="insn-00aae30c"></a> `00aae30c` | `2a 20 40 b9` | ldr w10,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00aae310"></a> `00aae310` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-00aae314"></a> `00aae314` | `6a 01 00 54` | b.ge 0x00aae340 | `CONDITIONAL_JUMP`
<a id="insn-00aae318"></a> `00aae318` | `0a 00 40 f9` | ldr x10,[x0] | `FALL_THROUGH`
<a id="insn-00aae31c"></a> `00aae31c` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00aae320"></a> `00aae320` | `5f 01 01 eb` | cmp x10,x1 | `FALL_THROUGH`
<a id="insn-00aae324"></a> `00aae324` | `20 02 00 54` | b.eq 0x00aae368 | `CONDITIONAL_JUMP`
<a id="insn-00aae328"></a> `00aae328` | `49 02 00 b4` | cbz x9,0x00aae370 | `CONDITIONAL_JUMP`
<a id="insn-00aae32c"></a> `00aae32c` | `ea 03 09 aa` | mov x10,x9 | `FALL_THROUGH`
<a id="insn-00aae330"></a> `00aae330` | `eb 03 0a aa` | mov x11,x10 | `FALL_THROUGH`
<a id="insn-00aae334"></a> `00aae334` | `4a 05 40 f9` | ldr x10,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-00aae338"></a> `00aae338` | `ca ff ff b5` | cbnz x10,0x00aae330 | `CONDITIONAL_JUMP`
<a id="insn-00aae33c"></a> `00aae33c` | `13 00 00 14` | b 0x00aae388 | `UNCONDITIONAL_JUMP`
<a id="insn-00aae340"></a> `00aae340` | `5f 01 09 6b` | cmp w10,w9 | `FALL_THROUGH`
<a id="insn-00aae344"></a> `00aae344` | `ea 05 00 54` | b.ge 0x00aae400 | `CONDITIONAL_JUMP`
<a id="insn-00aae348"></a> `00aae348` | `ea 03 01 aa` | mov x10,x1 | `FALL_THROUGH`
<a id="insn-00aae34c"></a> `00aae34c` | `4b 8d 40 f8` | ldr x11,[x10, #0x8]! | `FALL_THROUGH`
<a id="insn-00aae350"></a> `00aae350` | `0b 06 00 b4` | cbz x11,0x00aae410 | `CONDITIONAL_JUMP`
<a id="insn-00aae354"></a> `00aae354` | `ec 03 0b aa` | mov x12,x11 | `FALL_THROUGH`
<a id="insn-00aae358"></a> `00aae358` | `e3 03 0c aa` | mov x3,x12 | `FALL_THROUGH`
<a id="insn-00aae35c"></a> `00aae35c` | `8c 01 40 f9` | ldr x12,[x12] | `FALL_THROUGH`
<a id="insn-00aae360"></a> `00aae360` | `cc ff ff b5` | cbnz x12,0x00aae358 | `CONDITIONAL_JUMP`
<a id="insn-00aae364"></a> `00aae364` | `31 00 00 14` | b 0x00aae428 | `UNCONDITIONAL_JUMP`
<a id="insn-00aae368"></a> `00aae368` | `eb 03 01 aa` | mov x11,x1 | `FALL_THROUGH`
<a id="insn-00aae36c"></a> `00aae36c` | `0b 00 00 14` | b 0x00aae398 | `UNCONDITIONAL_JUMP`
<a id="insn-00aae370"></a> `00aae370` | `ea 03 01 aa` | mov x10,x1 | `FALL_THROUGH`
<a id="insn-00aae374"></a> `00aae374` | `4b 09 40 f9` | ldr x11,[x10, #0x10] | `FALL_THROUGH`
<a id="insn-00aae378"></a> `00aae378` | `6c 01 40 f9` | ldr x12,[x11] | `FALL_THROUGH`
<a id="insn-00aae37c"></a> `00aae37c` | `9f 01 0a eb` | cmp x12,x10 | `FALL_THROUGH`
<a id="insn-00aae380"></a> `00aae380` | `ea 03 0b aa` | mov x10,x11 | `FALL_THROUGH`
<a id="insn-00aae384"></a> `00aae384` | `80 ff ff 54` | b.eq 0x00aae374 | `CONDITIONAL_JUMP`
<a id="insn-00aae388"></a> `00aae388` | `6c 21 40 b9` | ldr w12,[x11, #0x20] | `FALL_THROUGH`
<a id="insn-00aae38c"></a> `00aae38c` | `8a 00 40 b9` | ldr w10,[x4] | `FALL_THROUGH`
<a id="insn-00aae390"></a> `00aae390` | `9f 01 0a 6b` | cmp w12,w10 | `FALL_THROUGH`
<a id="insn-00aae394"></a> `00aae394` | `aa 00 00 54` | b.ge 0x00aae3a8 | `CONDITIONAL_JUMP`
<a id="insn-00aae398"></a> `00aae398` | `e9 02 00 b4` | cbz x9,0x00aae3f4 | `CONDITIONAL_JUMP`
<a id="insn-00aae39c"></a> `00aae39c` | `60 21 00 91` | add x0,x11,#0x8 | `FALL_THROUGH`
<a id="insn-00aae3a0"></a> `00aae3a0` | `4b 00 00 f9` | str x11,[x2] | `FALL_THROUGH`
<a id="insn-00aae3a4"></a> `00aae3a4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aae3a8"></a> `00aae3a8` | `0b 01 40 f9` | ldr x11,[x8] | `FALL_THROUGH`
<a id="insn-00aae3ac"></a> `00aae3ac` | `cb 00 00 b5` | cbnz x11,0x00aae3c4 | `CONDITIONAL_JUMP`
<a id="insn-00aae3b0"></a> `00aae3b0` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00aae3b4"></a> `00aae3b4` | `0d 00 00 14` | b 0x00aae3e8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aae3b8"></a> `00aae3b8` | `2b 01 40 f9` | ldr x11,[x9] | `FALL_THROUGH`
<a id="insn-00aae3bc"></a> `00aae3bc` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00aae3c0"></a> `00aae3c0` | `4b 01 00 b4` | cbz x11,0x00aae3e8 | `CONDITIONAL_JUMP`
<a id="insn-00aae3c4"></a> `00aae3c4` | `e9 03 0b aa` | mov x9,x11 | `FALL_THROUGH`
<a id="insn-00aae3c8"></a> `00aae3c8` | `6b 21 40 b9` | ldr w11,[x11, #0x20] | `FALL_THROUGH`
<a id="insn-00aae3cc"></a> `00aae3cc` | `5f 01 0b 6b` | cmp w10,w11 | `FALL_THROUGH`
<a id="insn-00aae3d0"></a> `00aae3d0` | `4b ff ff 54` | b.lt 0x00aae3b8 | `CONDITIONAL_JUMP`
<a id="insn-00aae3d4"></a> `00aae3d4` | `7f 01 0a 6b` | cmp w11,w10 | `FALL_THROUGH`
<a id="insn-00aae3d8"></a> `00aae3d8` | `8a 00 00 54` | b.ge 0x00aae3e8 | `CONDITIONAL_JUMP`
<a id="insn-00aae3dc"></a> `00aae3dc` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00aae3e0"></a> `00aae3e0` | `0b 8d 40 f8` | ldr x11,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00aae3e4"></a> `00aae3e4` | `0b ff ff b5` | cbnz x11,0x00aae3c4 | `CONDITIONAL_JUMP`
<a id="insn-00aae3e8"></a> `00aae3e8` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aae3ec"></a> `00aae3ec` | `49 00 00 f9` | str x9,[x2] | `FALL_THROUGH`
<a id="insn-00aae3f0"></a> `00aae3f0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aae3f4"></a> `00aae3f4` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00aae3f8"></a> `00aae3f8` | `41 00 00 f9` | str x1,[x2] | `FALL_THROUGH`
<a id="insn-00aae3fc"></a> `00aae3fc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aae400"></a> `00aae400` | `e0 03 03 aa` | mov x0,x3 | `FALL_THROUGH`
<a id="insn-00aae404"></a> `00aae404` | `41 00 00 f9` | str x1,[x2] | `FALL_THROUGH`
<a id="insn-00aae408"></a> `00aae408` | `61 00 00 f9` | str x1,[x3] | `FALL_THROUGH`
<a id="insn-00aae40c"></a> `00aae40c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aae410"></a> `00aae410` | `ec 03 01 aa` | mov x12,x1 | `FALL_THROUGH`
<a id="insn-00aae414"></a> `00aae414` | `83 09 40 f9` | ldr x3,[x12, #0x10] | `FALL_THROUGH`
<a id="insn-00aae418"></a> `00aae418` | `6d 00 40 f9` | ldr x13,[x3] | `FALL_THROUGH`
<a id="insn-00aae41c"></a> `00aae41c` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00aae420"></a> `00aae420` | `ec 03 03 aa` | mov x12,x3 | `FALL_THROUGH`
<a id="insn-00aae424"></a> `00aae424` | `81 ff ff 54` | b.ne 0x00aae414 | `CONDITIONAL_JUMP`
<a id="insn-00aae428"></a> `00aae428` | `7f 00 08 eb` | cmp x3,x8 | `FALL_THROUGH`
<a id="insn-00aae42c"></a> `00aae42c` | `80 00 00 54` | b.eq 0x00aae43c | `CONDITIONAL_JUMP`
<a id="insn-00aae430"></a> `00aae430` | `6c 20 40 b9` | ldr w12,[x3, #0x20] | `FALL_THROUGH`
<a id="insn-00aae434"></a> `00aae434` | `3f 01 0c 6b` | cmp w9,w12 | `FALL_THROUGH`
<a id="insn-00aae438"></a> `00aae438` | `aa 00 00 54` | b.ge 0x00aae44c | `CONDITIONAL_JUMP`
<a id="insn-00aae43c"></a> `00aae43c` | `eb 02 00 b4` | cbz x11,0x00aae498 | `CONDITIONAL_JUMP`
<a id="insn-00aae440"></a> `00aae440` | `e0 03 03 aa` | mov x0,x3 | `FALL_THROUGH`
<a id="insn-00aae444"></a> `00aae444` | `43 00 00 f9` | str x3,[x2] | `FALL_THROUGH`
<a id="insn-00aae448"></a> `00aae448` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aae44c"></a> `00aae44c` | `0b 01 40 f9` | ldr x11,[x8] | `FALL_THROUGH`
<a id="insn-00aae450"></a> `00aae450` | `cb 00 00 b5` | cbnz x11,0x00aae468 | `CONDITIONAL_JUMP`
<a id="insn-00aae454"></a> `00aae454` | `ea 03 08 aa` | mov x10,x8 | `FALL_THROUGH`
<a id="insn-00aae458"></a> `00aae458` | `0d 00 00 14` | b 0x00aae48c | `UNCONDITIONAL_JUMP`
<a id="insn-00aae45c"></a> `00aae45c` | `4b 01 40 f9` | ldr x11,[x10] | `FALL_THROUGH`
<a id="insn-00aae460"></a> `00aae460` | `e8 03 0a aa` | mov x8,x10 | `FALL_THROUGH`
<a id="insn-00aae464"></a> `00aae464` | `4b 01 00 b4` | cbz x11,0x00aae48c | `CONDITIONAL_JUMP`
<a id="insn-00aae468"></a> `00aae468` | `ea 03 0b aa` | mov x10,x11 | `FALL_THROUGH`
<a id="insn-00aae46c"></a> `00aae46c` | `6b 21 40 b9` | ldr w11,[x11, #0x20] | `FALL_THROUGH`
<a id="insn-00aae470"></a> `00aae470` | `3f 01 0b 6b` | cmp w9,w11 | `FALL_THROUGH`
<a id="insn-00aae474"></a> `00aae474` | `4b ff ff 54` | b.lt 0x00aae45c | `CONDITIONAL_JUMP`
<a id="insn-00aae478"></a> `00aae478` | `7f 01 09 6b` | cmp w11,w9 | `FALL_THROUGH`
<a id="insn-00aae47c"></a> `00aae47c` | `8a 00 00 54` | b.ge 0x00aae48c | `CONDITIONAL_JUMP`
<a id="insn-00aae480"></a> `00aae480` | `e8 03 0a aa` | mov x8,x10 | `FALL_THROUGH`
<a id="insn-00aae484"></a> `00aae484` | `0b 8d 40 f8` | ldr x11,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00aae488"></a> `00aae488` | `0b ff ff b5` | cbnz x11,0x00aae468 | `CONDITIONAL_JUMP`
<a id="insn-00aae48c"></a> `00aae48c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aae490"></a> `00aae490` | `4a 00 00 f9` | str x10,[x2] | `FALL_THROUGH`
<a id="insn-00aae494"></a> `00aae494` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aae498"></a> `00aae498` | `e0 03 0a aa` | mov x0,x10 | `FALL_THROUGH`
<a id="insn-00aae49c"></a> `00aae49c` | `41 00 00 f9` | str x1,[x2] | `FALL_THROUGH`
<a id="insn-00aae4a0"></a> `00aae4a0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aae2fc`](#insn-00aae2fc) 範囲 `[['00aae2fc', '00aae307']]`
  - `CONDITIONAL_JUMP` [`00aae304`](#insn-00aae304) → [`00aae318`](#insn-00aae318)
  - `FALL_THROUGH` [`00aae304`](#insn-00aae304) → [`00aae308`](#insn-00aae308)
- ブロック [`00aae308`](#insn-00aae308) 範囲 `[['00aae308', '00aae317']]`
  - `CONDITIONAL_JUMP` [`00aae314`](#insn-00aae314) → [`00aae340`](#insn-00aae340)
  - `FALL_THROUGH` [`00aae314`](#insn-00aae314) → [`00aae318`](#insn-00aae318)
- ブロック [`00aae318`](#insn-00aae318) 範囲 `[['00aae318', '00aae327']]`
  - `CONDITIONAL_JUMP` [`00aae324`](#insn-00aae324) → [`00aae368`](#insn-00aae368)
  - `FALL_THROUGH` [`00aae324`](#insn-00aae324) → [`00aae328`](#insn-00aae328)
- ブロック [`00aae328`](#insn-00aae328) 範囲 `[['00aae328', '00aae32b']]`
  - `CONDITIONAL_JUMP` [`00aae328`](#insn-00aae328) → [`00aae370`](#insn-00aae370)
  - `FALL_THROUGH` [`00aae328`](#insn-00aae328) → [`00aae32c`](#insn-00aae32c)
- ブロック [`00aae32c`](#insn-00aae32c) 範囲 `[['00aae32c', '00aae32f']]`
  - `FALL_THROUGH` [`00aae32c`](#insn-00aae32c) → [`00aae330`](#insn-00aae330)
- ブロック [`00aae330`](#insn-00aae330) 範囲 `[['00aae330', '00aae33b']]`
  - `CONDITIONAL_JUMP` [`00aae338`](#insn-00aae338) → [`00aae330`](#insn-00aae330)
  - `FALL_THROUGH` [`00aae338`](#insn-00aae338) → [`00aae33c`](#insn-00aae33c)
- ブロック [`00aae33c`](#insn-00aae33c) 範囲 `[['00aae33c', '00aae33f']]`
  - `UNCONDITIONAL_JUMP` [`00aae33c`](#insn-00aae33c) → [`00aae388`](#insn-00aae388)
- ブロック [`00aae340`](#insn-00aae340) 範囲 `[['00aae340', '00aae347']]`
  - `CONDITIONAL_JUMP` [`00aae344`](#insn-00aae344) → [`00aae400`](#insn-00aae400)
  - `FALL_THROUGH` [`00aae344`](#insn-00aae344) → [`00aae348`](#insn-00aae348)
- ブロック [`00aae348`](#insn-00aae348) 範囲 `[['00aae348', '00aae353']]`
  - `CONDITIONAL_JUMP` [`00aae350`](#insn-00aae350) → [`00aae410`](#insn-00aae410)
  - `FALL_THROUGH` [`00aae350`](#insn-00aae350) → [`00aae354`](#insn-00aae354)
- ブロック [`00aae354`](#insn-00aae354) 範囲 `[['00aae354', '00aae357']]`
  - `FALL_THROUGH` [`00aae354`](#insn-00aae354) → [`00aae358`](#insn-00aae358)
- ブロック [`00aae358`](#insn-00aae358) 範囲 `[['00aae358', '00aae35f']]`
  - `FALL_THROUGH` [`00aae35c`](#insn-00aae35c) → [`00aae360`](#insn-00aae360)
- ブロック [`00aae360`](#insn-00aae360) 範囲 `[['00aae360', '00aae363']]`
  - `CONDITIONAL_JUMP` [`00aae360`](#insn-00aae360) → [`00aae358`](#insn-00aae358)
  - `FALL_THROUGH` [`00aae360`](#insn-00aae360) → [`00aae364`](#insn-00aae364)
- ブロック [`00aae364`](#insn-00aae364) 範囲 `[['00aae364', '00aae367']]`
  - `UNCONDITIONAL_JUMP` [`00aae364`](#insn-00aae364) → [`00aae428`](#insn-00aae428)
- ブロック [`00aae368`](#insn-00aae368) 範囲 `[['00aae368', '00aae36f']]`
  - `UNCONDITIONAL_JUMP` [`00aae36c`](#insn-00aae36c) → [`00aae398`](#insn-00aae398)
- ブロック [`00aae370`](#insn-00aae370) 範囲 `[['00aae370', '00aae373']]`
  - `FALL_THROUGH` [`00aae370`](#insn-00aae370) → [`00aae374`](#insn-00aae374)
- ブロック [`00aae374`](#insn-00aae374) 範囲 `[['00aae374', '00aae387']]`
  - `CONDITIONAL_JUMP` [`00aae384`](#insn-00aae384) → [`00aae374`](#insn-00aae374)
  - `FALL_THROUGH` [`00aae384`](#insn-00aae384) → [`00aae388`](#insn-00aae388)
- ブロック [`00aae388`](#insn-00aae388) 範囲 `[['00aae388', '00aae38f']]`
  - `FALL_THROUGH` [`00aae38c`](#insn-00aae38c) → [`00aae390`](#insn-00aae390)
- ブロック [`00aae390`](#insn-00aae390) 範囲 `[['00aae390', '00aae397']]`
  - `CONDITIONAL_JUMP` [`00aae394`](#insn-00aae394) → [`00aae3a8`](#insn-00aae3a8)
  - `FALL_THROUGH` [`00aae394`](#insn-00aae394) → [`00aae398`](#insn-00aae398)
- ブロック [`00aae398`](#insn-00aae398) 範囲 `[['00aae398', '00aae39b']]`
  - `CONDITIONAL_JUMP` [`00aae398`](#insn-00aae398) → [`00aae3f4`](#insn-00aae3f4)
  - `FALL_THROUGH` [`00aae398`](#insn-00aae398) → [`00aae39c`](#insn-00aae39c)
- ブロック [`00aae39c`](#insn-00aae39c) 範囲 `[['00aae39c', '00aae3a7']]`
- ブロック [`00aae3a8`](#insn-00aae3a8) 範囲 `[['00aae3a8', '00aae3af']]`
  - `CONDITIONAL_JUMP` [`00aae3ac`](#insn-00aae3ac) → [`00aae3c4`](#insn-00aae3c4)
  - `FALL_THROUGH` [`00aae3ac`](#insn-00aae3ac) → [`00aae3b0`](#insn-00aae3b0)
- ブロック [`00aae3b0`](#insn-00aae3b0) 範囲 `[['00aae3b0', '00aae3b7']]`
  - `UNCONDITIONAL_JUMP` [`00aae3b4`](#insn-00aae3b4) → [`00aae3e8`](#insn-00aae3e8)
- ブロック [`00aae3b8`](#insn-00aae3b8) 範囲 `[['00aae3b8', '00aae3c3']]`
  - `CONDITIONAL_JUMP` [`00aae3c0`](#insn-00aae3c0) → [`00aae3e8`](#insn-00aae3e8)
  - `FALL_THROUGH` [`00aae3c0`](#insn-00aae3c0) → [`00aae3c4`](#insn-00aae3c4)
- ブロック [`00aae3c4`](#insn-00aae3c4) 範囲 `[['00aae3c4', '00aae3cf']]`
  - `FALL_THROUGH` [`00aae3cc`](#insn-00aae3cc) → [`00aae3d0`](#insn-00aae3d0)
- ブロック [`00aae3d0`](#insn-00aae3d0) 範囲 `[['00aae3d0', '00aae3d3']]`
  - `CONDITIONAL_JUMP` [`00aae3d0`](#insn-00aae3d0) → [`00aae3b8`](#insn-00aae3b8)
  - `FALL_THROUGH` [`00aae3d0`](#insn-00aae3d0) → [`00aae3d4`](#insn-00aae3d4)
- ブロック [`00aae3d4`](#insn-00aae3d4) 範囲 `[['00aae3d4', '00aae3db']]`
  - `CONDITIONAL_JUMP` [`00aae3d8`](#insn-00aae3d8) → [`00aae3e8`](#insn-00aae3e8)
  - `FALL_THROUGH` [`00aae3d8`](#insn-00aae3d8) → [`00aae3dc`](#insn-00aae3dc)
- ブロック [`00aae3dc`](#insn-00aae3dc) 範囲 `[['00aae3dc', '00aae3e7']]`
  - `CONDITIONAL_JUMP` [`00aae3e4`](#insn-00aae3e4) → [`00aae3c4`](#insn-00aae3c4)
  - `FALL_THROUGH` [`00aae3e4`](#insn-00aae3e4) → [`00aae3e8`](#insn-00aae3e8)
- ブロック [`00aae3e8`](#insn-00aae3e8) 範囲 `[['00aae3e8', '00aae3f3']]`
- ブロック [`00aae3f4`](#insn-00aae3f4) 範囲 `[['00aae3f4', '00aae3ff']]`
- ブロック [`00aae400`](#insn-00aae400) 範囲 `[['00aae400', '00aae40f']]`
- ブロック [`00aae410`](#insn-00aae410) 範囲 `[['00aae410', '00aae413']]`
  - `FALL_THROUGH` [`00aae410`](#insn-00aae410) → [`00aae414`](#insn-00aae414)
- ブロック [`00aae414`](#insn-00aae414) 範囲 `[['00aae414', '00aae427']]`
  - `CONDITIONAL_JUMP` [`00aae424`](#insn-00aae424) → [`00aae414`](#insn-00aae414)
  - `FALL_THROUGH` [`00aae424`](#insn-00aae424) → [`00aae428`](#insn-00aae428)
- ブロック [`00aae428`](#insn-00aae428) 範囲 `[['00aae428', '00aae42f']]`
  - `CONDITIONAL_JUMP` [`00aae42c`](#insn-00aae42c) → [`00aae43c`](#insn-00aae43c)
  - `FALL_THROUGH` [`00aae42c`](#insn-00aae42c) → [`00aae430`](#insn-00aae430)
- ブロック [`00aae430`](#insn-00aae430) 範囲 `[['00aae430', '00aae43b']]`
  - `CONDITIONAL_JUMP` [`00aae438`](#insn-00aae438) → [`00aae44c`](#insn-00aae44c)
  - `FALL_THROUGH` [`00aae438`](#insn-00aae438) → [`00aae43c`](#insn-00aae43c)
- ブロック [`00aae43c`](#insn-00aae43c) 範囲 `[['00aae43c', '00aae43f']]`
  - `CONDITIONAL_JUMP` [`00aae43c`](#insn-00aae43c) → [`00aae498`](#insn-00aae498)
  - `FALL_THROUGH` [`00aae43c`](#insn-00aae43c) → [`00aae440`](#insn-00aae440)
- ブロック [`00aae440`](#insn-00aae440) 範囲 `[['00aae440', '00aae44b']]`
- ブロック [`00aae44c`](#insn-00aae44c) 範囲 `[['00aae44c', '00aae453']]`
  - `CONDITIONAL_JUMP` [`00aae450`](#insn-00aae450) → [`00aae468`](#insn-00aae468)
  - `FALL_THROUGH` [`00aae450`](#insn-00aae450) → [`00aae454`](#insn-00aae454)
- ブロック [`00aae454`](#insn-00aae454) 範囲 `[['00aae454', '00aae45b']]`
  - `UNCONDITIONAL_JUMP` [`00aae458`](#insn-00aae458) → [`00aae48c`](#insn-00aae48c)
- ブロック [`00aae45c`](#insn-00aae45c) 範囲 `[['00aae45c', '00aae467']]`
  - `CONDITIONAL_JUMP` [`00aae464`](#insn-00aae464) → [`00aae48c`](#insn-00aae48c)
  - `FALL_THROUGH` [`00aae464`](#insn-00aae464) → [`00aae468`](#insn-00aae468)
- ブロック [`00aae468`](#insn-00aae468) 範囲 `[['00aae468', '00aae477']]`
  - `CONDITIONAL_JUMP` [`00aae474`](#insn-00aae474) → [`00aae45c`](#insn-00aae45c)
  - `FALL_THROUGH` [`00aae474`](#insn-00aae474) → [`00aae478`](#insn-00aae478)
- ブロック [`00aae478`](#insn-00aae478) 範囲 `[['00aae478', '00aae47f']]`
  - `CONDITIONAL_JUMP` [`00aae47c`](#insn-00aae47c) → [`00aae48c`](#insn-00aae48c)
  - `FALL_THROUGH` [`00aae47c`](#insn-00aae47c) → [`00aae480`](#insn-00aae480)
- ブロック [`00aae480`](#insn-00aae480) 範囲 `[['00aae480', '00aae48b']]`
  - `CONDITIONAL_JUMP` [`00aae488`](#insn-00aae488) → [`00aae468`](#insn-00aae468)
  - `FALL_THROUGH` [`00aae488`](#insn-00aae488) → [`00aae48c`](#insn-00aae48c)
- ブロック [`00aae48c`](#insn-00aae48c) 範囲 `[['00aae48c', '00aae497']]`
- ブロック [`00aae498`](#insn-00aae498) 範囲 `[['00aae498', '00aae4a3']]`

## 命令位置別の参照

- [`00aae304`](#insn-00aae304) → [`00aae318`](#insn-00aae318) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae314`](#insn-00aae314) → [`00aae340`](#insn-00aae340) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae324`](#insn-00aae324) → [`00aae368`](#insn-00aae368) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae328`](#insn-00aae328) → [`00aae370`](#insn-00aae370) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae338`](#insn-00aae338) → [`00aae330`](#insn-00aae330) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae33c`](#insn-00aae33c) → [`00aae388`](#insn-00aae388) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae344`](#insn-00aae344) → [`00aae400`](#insn-00aae400) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae350`](#insn-00aae350) → [`00aae410`](#insn-00aae410) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae360`](#insn-00aae360) → [`00aae358`](#insn-00aae358) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae364`](#insn-00aae364) → [`00aae428`](#insn-00aae428) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae36c`](#insn-00aae36c) → [`00aae398`](#insn-00aae398) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae384`](#insn-00aae384) → [`00aae374`](#insn-00aae374) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae394`](#insn-00aae394) → [`00aae3a8`](#insn-00aae3a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae398`](#insn-00aae398) → [`00aae3f4`](#insn-00aae3f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae3ac`](#insn-00aae3ac) → [`00aae3c4`](#insn-00aae3c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae3b4`](#insn-00aae3b4) → [`00aae3e8`](#insn-00aae3e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae3c0`](#insn-00aae3c0) → [`00aae3e8`](#insn-00aae3e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae3d0`](#insn-00aae3d0) → [`00aae3b8`](#insn-00aae3b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae3d8`](#insn-00aae3d8) → [`00aae3e8`](#insn-00aae3e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae3e4`](#insn-00aae3e4) → [`00aae3c4`](#insn-00aae3c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae424`](#insn-00aae424) → [`00aae414`](#insn-00aae414) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae42c`](#insn-00aae42c) → [`00aae43c`](#insn-00aae43c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae438`](#insn-00aae438) → [`00aae44c`](#insn-00aae44c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae43c`](#insn-00aae43c) → [`00aae498`](#insn-00aae498) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae450`](#insn-00aae450) → [`00aae468`](#insn-00aae468) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae458`](#insn-00aae458) → [`00aae48c`](#insn-00aae48c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae464`](#insn-00aae464) → [`00aae48c`](#insn-00aae48c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae474`](#insn-00aae474) → [`00aae45c`](#insn-00aae45c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae47c`](#insn-00aae47c) → [`00aae48c`](#insn-00aae48c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae488`](#insn-00aae488) → [`00aae468`](#insn-00aae468) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aae304`](#insn-00aae304)

~~~json
{
  "source": "00aae304",
  "target": "00aae318",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae314`](#insn-00aae314)

~~~json
{
  "source": "00aae314",
  "target": "00aae340",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae324`](#insn-00aae324)

~~~json
{
  "source": "00aae324",
  "target": "00aae368",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae328`](#insn-00aae328)

~~~json
{
  "source": "00aae328",
  "target": "00aae370",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae338`](#insn-00aae338)

~~~json
{
  "source": "00aae338",
  "target": "00aae330",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae33c`](#insn-00aae33c)

~~~json
{
  "source": "00aae33c",
  "target": "00aae388",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae344`](#insn-00aae344)

~~~json
{
  "source": "00aae344",
  "target": "00aae400",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae350`](#insn-00aae350)

~~~json
{
  "source": "00aae350",
  "target": "00aae410",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae360`](#insn-00aae360)

~~~json
{
  "source": "00aae360",
  "target": "00aae358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae364`](#insn-00aae364)

~~~json
{
  "source": "00aae364",
  "target": "00aae428",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae36c`](#insn-00aae36c)

~~~json
{
  "source": "00aae36c",
  "target": "00aae398",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae384`](#insn-00aae384)

~~~json
{
  "source": "00aae384",
  "target": "00aae374",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae394`](#insn-00aae394)

~~~json
{
  "source": "00aae394",
  "target": "00aae3a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae398`](#insn-00aae398)

~~~json
{
  "source": "00aae398",
  "target": "00aae3f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae3ac`](#insn-00aae3ac)

~~~json
{
  "source": "00aae3ac",
  "target": "00aae3c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae3b4`](#insn-00aae3b4)

~~~json
{
  "source": "00aae3b4",
  "target": "00aae3e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae3c0`](#insn-00aae3c0)

~~~json
{
  "source": "00aae3c0",
  "target": "00aae3e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae3d0`](#insn-00aae3d0)

~~~json
{
  "source": "00aae3d0",
  "target": "00aae3b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae3d8`](#insn-00aae3d8)

~~~json
{
  "source": "00aae3d8",
  "target": "00aae3e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae3e4`](#insn-00aae3e4)

~~~json
{
  "source": "00aae3e4",
  "target": "00aae3c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae424`](#insn-00aae424)

~~~json
{
  "source": "00aae424",
  "target": "00aae414",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae42c`](#insn-00aae42c)

~~~json
{
  "source": "00aae42c",
  "target": "00aae43c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae438`](#insn-00aae438)

~~~json
{
  "source": "00aae438",
  "target": "00aae44c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae43c`](#insn-00aae43c)

~~~json
{
  "source": "00aae43c",
  "target": "00aae498",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae450`](#insn-00aae450)

~~~json
{
  "source": "00aae450",
  "target": "00aae468",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae458`](#insn-00aae458)

~~~json
{
  "source": "00aae458",
  "target": "00aae48c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae464`](#insn-00aae464)

~~~json
{
  "source": "00aae464",
  "target": "00aae48c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae474`](#insn-00aae474)

~~~json
{
  "source": "00aae474",
  "target": "00aae45c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae47c`](#insn-00aae47c)

~~~json
{
  "source": "00aae47c",
  "target": "00aae48c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae488`](#insn-00aae488)

~~~json
{
  "source": "00aae488",
  "target": "00aae468",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
