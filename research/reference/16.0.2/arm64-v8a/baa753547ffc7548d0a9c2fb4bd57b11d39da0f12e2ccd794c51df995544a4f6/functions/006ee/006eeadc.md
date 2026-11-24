# 006eeadc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0059.md#review-712273dca0353cfec38d8cf4463e1148)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `006eee8c`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ee/006eee8c.md) · 移動量 `+0x3b0`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0005.md#compare-0a51063ff8f952fb69116b8f060d2e51)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006eeadc",
  "name": "FUN_006eeadc",
  "size": 552,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ea308394b9be220edcabf06fb329efbae43f7c889698e383ecbbec128a7ec67e",
  "source_text_sha256": "ea308394b9be220edcabf06fb329efbae43f7c889698e383ecbbec128a7ec67e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006eeadc",
        "006eed03"
      ]
    ],
    "bytes_sha256": "27d6bc11945651365d11caeae54fb0b6f336d07f07aa6c7963137357064a02c9",
    "instruction_count": 138,
    "instruction_bytes": 552,
    "body_bytes": 552,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006eed04](../006ee/006eed04.md)

## 呼び出し先

- [0046d7f0](../0046d/0046d7f0.md)
- [006e4440](../006e4/006e4440.md)
- [006e4b1c](../006e4/006e4b1c.md)
- [00851550](../00851/00851550.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2245 bytes

~~~c

int FUN_006eeadc(long param_1)

{
  int iVar1;
  int iVar2;
  int iVar3;
  uint uVar4;
  int iVar5;
  int iVar6;
  undefined8 uVar7;
  undefined8 uVar8;
  long lVar9;
  undefined8 uVar10;
  undefined8 uVar11;
  int iVar12;
  int iVar13;
  
  uVar7 = FUN_0046d7f0(10000);
  uVar8 = FUN_006e4b1c(uVar7,*(undefined4 *)(param_1 + 0x1f88),7);
  iVar3 = FUN_006e4b1c(uVar8,*(undefined4 *)(param_1 + 0x1f88),7);
  uVar4 = FUN_006e4440();
  lVar9 = FUN_00851550();
  if (uVar4 < 0x47) {
    lVar9 = FUN_00851550();
    iVar5 = *(int *)(BYTE_ARRAY_0043ade1 + lVar9 + (ulong)uVar4 * 4 + 0x13);
  }
  else {
    iVar5 = 0;
  }
  iVar12 = 0;
  iVar13 = 0;
  iVar1 = 0;
  if (iVar5 + iVar3 != 0) {
    iVar1 = ((int)uVar8 * 100) / (iVar5 + iVar3);
  }
  iVar3 = 0x12;
  do {
    uVar8 = FUN_006e4b1c(lVar9,*(undefined4 *)(param_1 + 0x1f88),iVar3 + -9);
    uVar10 = FUN_006e4b1c(uVar8,*(undefined4 *)(param_1 + 0x1f88),iVar3 + -10);
    iVar2 = (int)uVar10;
    iVar5 = FUN_006e4b1c(uVar10,*(undefined4 *)(param_1 + 0x1f88),iVar3 + -6);
    lVar9 = FUN_00851550();
    iVar5 = (*(int *)(BYTE_ARRAY_0043a5a9 + lVar9 + (long)*(int *)(param_1 + 0x1f9c) * 0x10 + 0x2f)
            * iVar5) / 100;
    if (iVar3 == 0x2a) {
      if ((int)uVar8 == 0x16) {
LAB_006eec40:
        iVar5 = (iVar5 + iVar2) * iVar1;
LAB_006eec58:
        iVar5 = iVar5 / 100;
      }
      else {
        iVar5 = iVar5 + iVar2;
      }
      iVar13 = iVar5 + iVar13;
    }
    else {
      uVar10 = FUN_006e4b1c(lVar9,*(undefined4 *)(param_1 + 0x1f88),iVar3 + -3);
      uVar11 = FUN_006e4b1c(uVar10,*(undefined4 *)(param_1 + 0x1f88),iVar3 + -4);
      iVar6 = FUN_006e4b1c(uVar11,*(undefined4 *)(param_1 + 0x1f88),iVar3);
      lVar9 = FUN_00851550();
      if ((int)uVar8 == 0x16) goto LAB_006eec40;
      iVar13 = iVar5 + iVar2 + iVar13;
      if ((int)uVar10 == 0x16) {
        iVar5 = ((*(int *)(BYTE_ARRAY_0043a5a9 +
                          lVar9 + (long)*(int *)(param_1 + 0x1f9c) * 0x10 + 0x2f) * iVar6) / 100 +
                (int)uVar11) * (100 - iVar1);
        goto LAB_006eec58;
      }
    }
    if ((int)uVar7 < iVar13) {
      return iVar12;
    }
    iVar3 = iVar3 + 6;
    iVar12 = iVar12 + 1;
    if (iVar3 == 0x30) {
      return -1;
    }
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006eeadc"></a> `006eeadc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-006eeae0"></a> `006eeae0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006eeae4"></a> `006eeae4` | `fc 6f 02 a9` | stp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006eeae8"></a> `006eeae8` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006eeaec"></a> `006eeaec` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006eeaf0"></a> `006eeaf0` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-006eeaf4"></a> `006eeaf4` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-006eeaf8"></a> `006eeaf8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-006eeafc"></a> `006eeafc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-006eeb00"></a> `006eeb00` | `00 e2 84 52` | mov w0,#0x2710 | `FALL_THROUGH`
<a id="insn-006eeb04"></a> `006eeb04` | `3b fb f5 97` | bl 0x0046d7f0 | `UNCONDITIONAL_CALL`
<a id="insn-006eeb08"></a> `006eeb08` | `61 8a 5f b9` | ldr w1,[x19, #0x1f88] | `FALL_THROUGH`
<a id="insn-006eeb0c"></a> `006eeb0c` | `e2 00 80 52` | mov w2,#0x7 | `FALL_THROUGH`
<a id="insn-006eeb10"></a> `006eeb10` | `a0 c3 1f b8` | stur w0,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-006eeb14"></a> `006eeb14` | `02 d8 ff 97` | bl 0x006e4b1c | `UNCONDITIONAL_CALL`
<a id="insn-006eeb18"></a> `006eeb18` | `61 8a 5f b9` | ldr w1,[x19, #0x1f88] | `FALL_THROUGH`
<a id="insn-006eeb1c"></a> `006eeb1c` | `94 0c 80 52` | mov w20,#0x64 | `FALL_THROUGH`
<a id="insn-006eeb20"></a> `006eeb20` | `e2 00 80 52` | mov w2,#0x7 | `FALL_THROUGH`
<a id="insn-006eeb24"></a> `006eeb24` | `17 7c 14 1b` | mul w23,w0,w20 | `FALL_THROUGH`
<a id="insn-006eeb28"></a> `006eeb28` | `fd d7 ff 97` | bl 0x006e4b1c | `UNCONDITIONAL_CALL`
<a id="insn-006eeb2c"></a> `006eeb2c` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-006eeb30"></a> `006eeb30` | `44 d6 ff 97` | bl 0x006e4440 | `UNCONDITIONAL_CALL`
<a id="insn-006eeb34"></a> `006eeb34` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-006eeb38"></a> `006eeb38` | `86 8a 05 94` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-006eeb3c"></a> `006eeb3c` | `bf 1a 01 71` | cmp w21,#0x46 | `FALL_THROUGH`
<a id="insn-006eeb40"></a> `006eeb40` | `e8 00 00 54` | b.hi 0x006eeb5c | `CONDITIONAL_JUMP`
<a id="insn-006eeb44"></a> `006eeb44` | `83 8a 05 94` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-006eeb48"></a> `006eeb48` | `08 48 35 8b` | add x8,x0,w21, UXTW  #0x2 | `FALL_THROUGH`
<a id="insn-006eeb4c"></a> `006eeb4c` | `89 be 95 52` | mov w9,#0xadf4 | `FALL_THROUGH`
<a id="insn-006eeb50"></a> `006eeb50` | `69 08 a0 72` | movk w9,#0x43, LSL #16 | `FALL_THROUGH`
<a id="insn-006eeb54"></a> `006eeb54` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006eeb58"></a> `006eeb58` | `02 00 00 14` | b 0x006eeb60 | `UNCONDITIONAL_JUMP`
<a id="insn-006eeb5c"></a> `006eeb5c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-006eeb60"></a> `006eeb60` | `08 01 16 0b` | add w8,w8,w22 | `FALL_THROUGH`
<a id="insn-006eeb64"></a> `006eeb64` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-006eeb68"></a> `006eeb68` | `fc 03 1f 2a` | mov w28,wzr | `FALL_THROUGH`
<a id="insn-006eeb6c"></a> `006eeb6c` | `e8 0e c8 1a` | sdiv w8,w23,w8 | `FALL_THROUGH`
<a id="insn-006eeb70"></a> `006eeb70` | `56 02 80 52` | mov w22,#0x12 | `FALL_THROUGH`
<a id="insn-006eeb74"></a> `006eeb74` | `e8 0b 00 b9` | str w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006eeb78"></a> `006eeb78` | `88 02 08 4b` | sub w8,w20,w8 | `FALL_THROUGH`
<a id="insn-006eeb7c"></a> `006eeb7c` | `e8 07 00 b9` | str w8,[sp, #0x4] | `FALL_THROUGH`
<a id="insn-006eeb80"></a> `006eeb80` | `61 8a 5f b9` | ldr w1,[x19, #0x1f88] | `FALL_THROUGH`
<a id="insn-006eeb84"></a> `006eeb84` | `c2 26 00 51` | sub w2,w22,#0x9 | `FALL_THROUGH`
<a id="insn-006eeb88"></a> `006eeb88` | `d7 2a 00 51` | sub w23,w22,#0xa | `FALL_THROUGH`
<a id="insn-006eeb8c"></a> `006eeb8c` | `e4 d7 ff 97` | bl 0x006e4b1c | `UNCONDITIONAL_CALL`
<a id="insn-006eeb90"></a> `006eeb90` | `61 8a 5f b9` | ldr w1,[x19, #0x1f88] | `FALL_THROUGH`
<a id="insn-006eeb94"></a> `006eeb94` | `e2 03 17 2a` | mov w2,w23 | `FALL_THROUGH`
<a id="insn-006eeb98"></a> `006eeb98` | `f8 03 00 2a` | mov w24,w0 | `FALL_THROUGH`
<a id="insn-006eeb9c"></a> `006eeb9c` | `e0 d7 ff 97` | bl 0x006e4b1c | `UNCONDITIONAL_CALL`
<a id="insn-006eeba0"></a> `006eeba0` | `61 8a 5f b9` | ldr w1,[x19, #0x1f88] | `FALL_THROUGH`
<a id="insn-006eeba4"></a> `006eeba4` | `c2 1a 00 51` | sub w2,w22,#0x6 | `FALL_THROUGH`
<a id="insn-006eeba8"></a> `006eeba8` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-006eebac"></a> `006eebac` | `dc d7 ff 97` | bl 0x006e4b1c | `UNCONDITIONAL_CALL`
<a id="insn-006eebb0"></a> `006eebb0` | `f9 03 00 2a` | mov w25,w0 | `FALL_THROUGH`
<a id="insn-006eebb4"></a> `006eebb4` | `67 8a 05 94` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-006eebb8"></a> `006eebb8` | `68 9e 9f b9` | ldrsw x8,[x19, #0x1f9c] | `FALL_THROUGH`
<a id="insn-006eebbc"></a> `006eebbc` | `09 bb 94 52` | mov w9,#0xa5d8 | `FALL_THROUGH`
<a id="insn-006eebc0"></a> `006eebc0` | `df aa 00 71` | cmp w22,#0x2a | `FALL_THROUGH`
<a id="insn-006eebc4"></a> `006eebc4` | `69 08 a0 72` | movk w9,#0x43, LSL #16 | `FALL_THROUGH`
<a id="insn-006eebc8"></a> `006eebc8` | `08 10 08 8b` | add x8,x0,x8, LSL #0x4 | `FALL_THROUGH`
<a id="insn-006eebcc"></a> `006eebcc` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006eebd0"></a> `006eebd0` | `e9 a3 90 52` | mov w9,#0x851f | `FALL_THROUGH`
<a id="insn-006eebd4"></a> `006eebd4` | `69 3d aa 72` | movk w9,#0x51eb, LSL #16 | `FALL_THROUGH`
<a id="insn-006eebd8"></a> `006eebd8` | `08 7d 19 1b` | mul w8,w8,w25 | `FALL_THROUGH`
<a id="insn-006eebdc"></a> `006eebdc` | `08 7d 29 9b` | smull x8,w8,w9 | `FALL_THROUGH`
<a id="insn-006eebe0"></a> `006eebe0` | `09 fd 7f d3` | lsr x9,x8,#0x3f | `FALL_THROUGH`
<a id="insn-006eebe4"></a> `006eebe4` | `08 fd 65 93` | asr x8,x8,#0x25 | `FALL_THROUGH`
<a id="insn-006eebe8"></a> `006eebe8` | `14 01 09 0b` | add w20,w8,w9 | `FALL_THROUGH`
<a id="insn-006eebec"></a> `006eebec` | `a1 00 00 54` | b.ne 0x006eec00 | `CONDITIONAL_JUMP`
<a id="insn-006eebf0"></a> `006eebf0` | `1f 5b 00 71` | cmp w24,#0x16 | `FALL_THROUGH`
<a id="insn-006eebf4"></a> `006eebf4` | `60 02 00 54` | b.eq 0x006eec40 | `CONDITIONAL_JUMP`
<a id="insn-006eebf8"></a> `006eebf8` | `88 02 17 0b` | add w8,w20,w23 | `FALL_THROUGH`
<a id="insn-006eebfc"></a> `006eebfc` | `1a 00 00 14` | b 0x006eec64 | `UNCONDITIONAL_JUMP`
<a id="insn-006eec00"></a> `006eec00` | `61 8a 5f b9` | ldr w1,[x19, #0x1f88] | `FALL_THROUGH`
<a id="insn-006eec04"></a> `006eec04` | `c2 0e 00 51` | sub w2,w22,#0x3 | `FALL_THROUGH`
<a id="insn-006eec08"></a> `006eec08` | `d9 12 00 51` | sub w25,w22,#0x4 | `FALL_THROUGH`
<a id="insn-006eec0c"></a> `006eec0c` | `c4 d7 ff 97` | bl 0x006e4b1c | `UNCONDITIONAL_CALL`
<a id="insn-006eec10"></a> `006eec10` | `61 8a 5f b9` | ldr w1,[x19, #0x1f88] | `FALL_THROUGH`
<a id="insn-006eec14"></a> `006eec14` | `e2 03 19 2a` | mov w2,w25 | `FALL_THROUGH`
<a id="insn-006eec18"></a> `006eec18` | `fa 03 00 2a` | mov w26,w0 | `FALL_THROUGH`
<a id="insn-006eec1c"></a> `006eec1c` | `c0 d7 ff 97` | bl 0x006e4b1c | `UNCONDITIONAL_CALL`
<a id="insn-006eec20"></a> `006eec20` | `61 8a 5f b9` | ldr w1,[x19, #0x1f88] | `FALL_THROUGH`
<a id="insn-006eec24"></a> `006eec24` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-006eec28"></a> `006eec28` | `f9 03 00 2a` | mov w25,w0 | `FALL_THROUGH`
<a id="insn-006eec2c"></a> `006eec2c` | `bc d7 ff 97` | bl 0x006e4b1c | `UNCONDITIONAL_CALL`
<a id="insn-006eec30"></a> `006eec30` | `fb 03 00 2a` | mov w27,w0 | `FALL_THROUGH`
<a id="insn-006eec34"></a> `006eec34` | `47 8a 05 94` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-006eec38"></a> `006eec38` | `1f 5b 00 71` | cmp w24,#0x16 | `FALL_THROUGH`
<a id="insn-006eec3c"></a> `006eec3c` | `61 02 00 54` | b.ne 0x006eec88 | `CONDITIONAL_JUMP`
<a id="insn-006eec40"></a> `006eec40` | `e9 0b 40 b9` | ldr w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006eec44"></a> `006eec44` | `88 02 17 0b` | add w8,w20,w23 | `FALL_THROUGH`
<a id="insn-006eec48"></a> `006eec48` | `08 7d 09 1b` | mul w8,w8,w9 | `FALL_THROUGH`
<a id="insn-006eec4c"></a> `006eec4c` | `e9 a3 90 52` | mov w9,#0x851f | `FALL_THROUGH`
<a id="insn-006eec50"></a> `006eec50` | `69 3d aa 72` | movk w9,#0x51eb, LSL #16 | `FALL_THROUGH`
<a id="insn-006eec54"></a> `006eec54` | `08 7d 29 9b` | smull x8,w8,w9 | `FALL_THROUGH`
<a id="insn-006eec58"></a> `006eec58` | `09 fd 7f d3` | lsr x9,x8,#0x3f | `FALL_THROUGH`
<a id="insn-006eec5c"></a> `006eec5c` | `08 fd 65 93` | asr x8,x8,#0x25 | `FALL_THROUGH`
<a id="insn-006eec60"></a> `006eec60` | `08 01 09 0b` | add w8,w8,w9 | `FALL_THROUGH`
<a id="insn-006eec64"></a> `006eec64` | `1c 01 1c 0b` | add w28,w8,w28 | `FALL_THROUGH`
<a id="insn-006eec68"></a> `006eec68` | `a8 c3 5f b8` | ldur w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-006eec6c"></a> `006eec6c` | `1f 01 1c 6b` | cmp w8,w28 | `FALL_THROUGH`
<a id="insn-006eec70"></a> `006eec70` | `8b 03 00 54` | b.lt 0x006eece0 | `CONDITIONAL_JUMP`
<a id="insn-006eec74"></a> `006eec74` | `d6 1a 00 11` | add w22,w22,#0x6 | `FALL_THROUGH`
<a id="insn-006eec78"></a> `006eec78` | `b5 06 00 11` | add w21,w21,#0x1 | `FALL_THROUGH`
<a id="insn-006eec7c"></a> `006eec7c` | `df c2 00 71` | cmp w22,#0x30 | `FALL_THROUGH`
<a id="insn-006eec80"></a> `006eec80` | `01 f8 ff 54` | b.ne 0x006eeb80 | `CONDITIONAL_JUMP`
<a id="insn-006eec84"></a> `006eec84` | `16 00 00 14` | b 0x006eecdc | `UNCONDITIONAL_JUMP`
<a id="insn-006eec88"></a> `006eec88` | `88 02 17 0b` | add w8,w20,w23 | `FALL_THROUGH`
<a id="insn-006eec8c"></a> `006eec8c` | `5f 5b 00 71` | cmp w26,#0x16 | `FALL_THROUGH`
<a id="insn-006eec90"></a> `006eec90` | `1c 01 1c 0b` | add w28,w8,w28 | `FALL_THROUGH`
<a id="insn-006eec94"></a> `006eec94` | `a1 fe ff 54` | b.ne 0x006eec68 | `CONDITIONAL_JUMP`
<a id="insn-006eec98"></a> `006eec98` | `68 9e 9f b9` | ldrsw x8,[x19, #0x1f9c] | `FALL_THROUGH`
<a id="insn-006eec9c"></a> `006eec9c` | `09 bb 94 52` | mov w9,#0xa5d8 | `FALL_THROUGH`
<a id="insn-006eeca0"></a> `006eeca0` | `ea a3 90 52` | mov w10,#0x851f | `FALL_THROUGH`
<a id="insn-006eeca4"></a> `006eeca4` | `69 08 a0 72` | movk w9,#0x43, LSL #16 | `FALL_THROUGH`
<a id="insn-006eeca8"></a> `006eeca8` | `6a 3d aa 72` | movk w10,#0x51eb, LSL #16 | `FALL_THROUGH`
<a id="insn-006eecac"></a> `006eecac` | `08 10 08 8b` | add x8,x0,x8, LSL #0x4 | `FALL_THROUGH`
<a id="insn-006eecb0"></a> `006eecb0` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006eecb4"></a> `006eecb4` | `08 7d 1b 1b` | mul w8,w8,w27 | `FALL_THROUGH`
<a id="insn-006eecb8"></a> `006eecb8` | `08 7d 2a 9b` | smull x8,w8,w10 | `FALL_THROUGH`
<a id="insn-006eecbc"></a> `006eecbc` | `09 fd 7f d3` | lsr x9,x8,#0x3f | `FALL_THROUGH`
<a id="insn-006eecc0"></a> `006eecc0` | `08 fd 65 93` | asr x8,x8,#0x25 | `FALL_THROUGH`
<a id="insn-006eecc4"></a> `006eecc4` | `08 01 09 0b` | add w8,w8,w9 | `FALL_THROUGH`
<a id="insn-006eecc8"></a> `006eecc8` | `e9 07 40 b9` | ldr w9,[sp, #0x4] | `FALL_THROUGH`
<a id="insn-006eeccc"></a> `006eeccc` | `08 01 19 0b` | add w8,w8,w25 | `FALL_THROUGH`
<a id="insn-006eecd0"></a> `006eecd0` | `08 7d 09 1b` | mul w8,w8,w9 | `FALL_THROUGH`
<a id="insn-006eecd4"></a> `006eecd4` | `08 7d 2a 9b` | smull x8,w8,w10 | `FALL_THROUGH`
<a id="insn-006eecd8"></a> `006eecd8` | `e0 ff ff 17` | b 0x006eec58 | `UNCONDITIONAL_JUMP`
<a id="insn-006eecdc"></a> `006eecdc` | `15 00 80 12` | mov w21,#0xffffffff | `FALL_THROUGH`
<a id="insn-006eece0"></a> `006eece0` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-006eece4"></a> `006eece4` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-006eece8"></a> `006eece8` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-006eecec"></a> `006eecec` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006eecf0"></a> `006eecf0` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006eecf4"></a> `006eecf4` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006eecf8"></a> `006eecf8` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006eecfc"></a> `006eecfc` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-006eed00"></a> `006eed00` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006eeadc`](#insn-006eeadc) 範囲 `[['006eeadc', '006eeb43']]`
  - `CONDITIONAL_JUMP` [`006eeb40`](#insn-006eeb40) → [`006eeb5c`](#insn-006eeb5c)
  - `FALL_THROUGH` [`006eeb40`](#insn-006eeb40) → [`006eeb44`](#insn-006eeb44)
- ブロック [`006eeb44`](#insn-006eeb44) 範囲 `[['006eeb44', '006eeb5b']]`
  - `UNCONDITIONAL_JUMP` [`006eeb58`](#insn-006eeb58) → [`006eeb60`](#insn-006eeb60)
- ブロック [`006eeb5c`](#insn-006eeb5c) 範囲 `[['006eeb5c', '006eeb5f']]`
  - `FALL_THROUGH` [`006eeb5c`](#insn-006eeb5c) → [`006eeb60`](#insn-006eeb60)
- ブロック [`006eeb60`](#insn-006eeb60) 範囲 `[['006eeb60', '006eeb7f']]`
  - `FALL_THROUGH` [`006eeb7c`](#insn-006eeb7c) → [`006eeb80`](#insn-006eeb80)
- ブロック [`006eeb80`](#insn-006eeb80) 範囲 `[['006eeb80', '006eebef']]`
  - `CONDITIONAL_JUMP` [`006eebec`](#insn-006eebec) → [`006eec00`](#insn-006eec00)
  - `FALL_THROUGH` [`006eebec`](#insn-006eebec) → [`006eebf0`](#insn-006eebf0)
- ブロック [`006eebf0`](#insn-006eebf0) 範囲 `[['006eebf0', '006eebf7']]`
  - `CONDITIONAL_JUMP` [`006eebf4`](#insn-006eebf4) → [`006eec40`](#insn-006eec40)
  - `FALL_THROUGH` [`006eebf4`](#insn-006eebf4) → [`006eebf8`](#insn-006eebf8)
- ブロック [`006eebf8`](#insn-006eebf8) 範囲 `[['006eebf8', '006eebff']]`
  - `UNCONDITIONAL_JUMP` [`006eebfc`](#insn-006eebfc) → [`006eec64`](#insn-006eec64)
- ブロック [`006eec00`](#insn-006eec00) 範囲 `[['006eec00', '006eec3f']]`
  - `CONDITIONAL_JUMP` [`006eec3c`](#insn-006eec3c) → [`006eec88`](#insn-006eec88)
  - `FALL_THROUGH` [`006eec3c`](#insn-006eec3c) → [`006eec40`](#insn-006eec40)
- ブロック [`006eec40`](#insn-006eec40) 範囲 `[['006eec40', '006eec57']]`
  - `FALL_THROUGH` [`006eec54`](#insn-006eec54) → [`006eec58`](#insn-006eec58)
- ブロック [`006eec58`](#insn-006eec58) 範囲 `[['006eec58', '006eec63']]`
  - `FALL_THROUGH` [`006eec60`](#insn-006eec60) → [`006eec64`](#insn-006eec64)
- ブロック [`006eec64`](#insn-006eec64) 範囲 `[['006eec64', '006eec67']]`
  - `FALL_THROUGH` [`006eec64`](#insn-006eec64) → [`006eec68`](#insn-006eec68)
- ブロック [`006eec68`](#insn-006eec68) 範囲 `[['006eec68', '006eec73']]`
  - `CONDITIONAL_JUMP` [`006eec70`](#insn-006eec70) → [`006eece0`](#insn-006eece0)
  - `FALL_THROUGH` [`006eec70`](#insn-006eec70) → [`006eec74`](#insn-006eec74)
- ブロック [`006eec74`](#insn-006eec74) 範囲 `[['006eec74', '006eec83']]`
  - `CONDITIONAL_JUMP` [`006eec80`](#insn-006eec80) → [`006eeb80`](#insn-006eeb80)
  - `FALL_THROUGH` [`006eec80`](#insn-006eec80) → [`006eec84`](#insn-006eec84)
- ブロック [`006eec84`](#insn-006eec84) 範囲 `[['006eec84', '006eec87']]`
  - `UNCONDITIONAL_JUMP` [`006eec84`](#insn-006eec84) → [`006eecdc`](#insn-006eecdc)
- ブロック [`006eec88`](#insn-006eec88) 範囲 `[['006eec88', '006eec97']]`
  - `CONDITIONAL_JUMP` [`006eec94`](#insn-006eec94) → [`006eec68`](#insn-006eec68)
  - `FALL_THROUGH` [`006eec94`](#insn-006eec94) → [`006eec98`](#insn-006eec98)
- ブロック [`006eec98`](#insn-006eec98) 範囲 `[['006eec98', '006eecdb']]`
  - `UNCONDITIONAL_JUMP` [`006eecd8`](#insn-006eecd8) → [`006eec58`](#insn-006eec58)
- ブロック [`006eecdc`](#insn-006eecdc) 範囲 `[['006eecdc', '006eecdf']]`
  - `FALL_THROUGH` [`006eecdc`](#insn-006eecdc) → [`006eece0`](#insn-006eece0)
- ブロック [`006eece0`](#insn-006eece0) 範囲 `[['006eece0', '006eed03']]`

## 命令位置別の参照

- [`006eeae0`](#insn-006eeae0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eeae4`](#insn-006eeae4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eeae8`](#insn-006eeae8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eeaec`](#insn-006eeaec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eeaf0`](#insn-006eeaf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eeaf4`](#insn-006eeaf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eeb04`](#insn-006eeb04) → [`0046d7f0`](../0046d/0046d7f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046d7f0` · 推定シンボル `None` · 推定型 `None`
- [`006eeb10`](#insn-006eeb10) → `Stack[-0x64]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eeb14`](#insn-006eeb14) → [`006e4b1c`](../006e4/006e4b1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006e4b1c` · 推定シンボル `None` · 推定型 `None`
- [`006eeb28`](#insn-006eeb28) → [`006e4b1c`](../006e4/006e4b1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006e4b1c` · 推定シンボル `None` · 推定型 `None`
- [`006eeb30`](#insn-006eeb30) → [`006e4440`](../006e4/006e4440.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006e4440` · 推定シンボル `None` · 推定型 `None`
- [`006eeb38`](#insn-006eeb38) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`006eeb40`](#insn-006eeb40) → [`006eeb5c`](#insn-006eeb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eeb44`](#insn-006eeb44) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`006eeb54`](#insn-006eeb54) → `0043adf4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[35]`
- [`006eeb58`](#insn-006eeb58) → [`006eeb60`](#insn-006eeb60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eeb74`](#insn-006eeb74) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eeb7c`](#insn-006eeb7c) → `Stack[-0x6c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eeb8c`](#insn-006eeb8c) → [`006e4b1c`](../006e4/006e4b1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006e4b1c` · 推定シンボル `None` · 推定型 `None`
- [`006eeb9c`](#insn-006eeb9c) → [`006e4b1c`](../006e4/006e4b1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006e4b1c` · 推定シンボル `None` · 推定型 `None`
- [`006eebac`](#insn-006eebac) → [`006e4b1c`](../006e4/006e4b1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006e4b1c` · 推定シンボル `None` · 推定型 `None`
- [`006eebb4`](#insn-006eebb4) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`006eebcc`](#insn-006eebcc) → `0043a5d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[259]`
- [`006eebec`](#insn-006eebec) → [`006eec00`](#insn-006eec00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eebf4`](#insn-006eebf4) → [`006eec40`](#insn-006eec40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eebfc`](#insn-006eebfc) → [`006eec64`](#insn-006eec64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eec0c`](#insn-006eec0c) → [`006e4b1c`](../006e4/006e4b1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006e4b1c` · 推定シンボル `None` · 推定型 `None`
- [`006eec1c`](#insn-006eec1c) → [`006e4b1c`](../006e4/006e4b1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006e4b1c` · 推定シンボル `None` · 推定型 `None`
- [`006eec2c`](#insn-006eec2c) → [`006e4b1c`](../006e4/006e4b1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006e4b1c` · 推定シンボル `None` · 推定型 `None`
- [`006eec34`](#insn-006eec34) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`006eec3c`](#insn-006eec3c) → [`006eec88`](#insn-006eec88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eec40`](#insn-006eec40) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eec68`](#insn-006eec68) → `Stack[-0x64]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eec70`](#insn-006eec70) → [`006eece0`](#insn-006eece0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eec80`](#insn-006eec80) → [`006eeb80`](#insn-006eeb80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eec84`](#insn-006eec84) → [`006eecdc`](#insn-006eecdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eec94`](#insn-006eec94) → [`006eec68`](#insn-006eec68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eecb0`](#insn-006eecb0) → `0043a5d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[259]`
- [`006eecc8`](#insn-006eecc8) → `Stack[-0x6c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eecd8`](#insn-006eecd8) → [`006eec58`](#insn-006eec58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eece4`](#insn-006eece4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eece8`](#insn-006eece8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eecec`](#insn-006eecec) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eecf0`](#insn-006eecf0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eecf4`](#insn-006eecf4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eecf8`](#insn-006eecf8) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006eeae0`](#insn-006eeae0)

~~~json
{
  "source": "006eeae0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eeae4`](#insn-006eeae4)

~~~json
{
  "source": "006eeae4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eeae8`](#insn-006eeae8)

~~~json
{
  "source": "006eeae8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eeaec`](#insn-006eeaec)

~~~json
{
  "source": "006eeaec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eeaf0`](#insn-006eeaf0)

~~~json
{
  "source": "006eeaf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eeaf4`](#insn-006eeaf4)

~~~json
{
  "source": "006eeaf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eeb04`](#insn-006eeb04)

~~~json
{
  "source": "006eeb04",
  "target": "0046d7f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006eeb10`](#insn-006eeb10)

~~~json
{
  "source": "006eeb10",
  "target": "Stack[-0x64]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eeb14`](#insn-006eeb14)

~~~json
{
  "source": "006eeb14",
  "target": "006e4b1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006eeb28`](#insn-006eeb28)

~~~json
{
  "source": "006eeb28",
  "target": "006e4b1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006eeb30`](#insn-006eeb30)

~~~json
{
  "source": "006eeb30",
  "target": "006e4440",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006eeb38`](#insn-006eeb38)

~~~json
{
  "source": "006eeb38",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006eeb40`](#insn-006eeb40)

~~~json
{
  "source": "006eeb40",
  "target": "006eeb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eeb44`](#insn-006eeb44)

~~~json
{
  "source": "006eeb44",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006eeb54`](#insn-006eeb54)

~~~json
{
  "source": "006eeb54",
  "target": "0043adf4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0043ade1",
  "offset": 19,
  "size": 35,
  "datatype": "byte[35]",
  "bytes": "442d440e20480c1d20930294049e069d080a02e00c1f20480e00442dd3d4dedd",
  "capture_start": "0043ade1",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006eeb58`](#insn-006eeb58)

~~~json
{
  "source": "006eeb58",
  "target": "006eeb60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eeb74`](#insn-006eeb74)

~~~json
{
  "source": "006eeb74",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eeb7c`](#insn-006eeb7c)

~~~json
{
  "source": "006eeb7c",
  "target": "Stack[-0x6c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eeb8c`](#insn-006eeb8c)

~~~json
{
  "source": "006eeb8c",
  "target": "006e4b1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006eeb9c`](#insn-006eeb9c)

~~~json
{
  "source": "006eeb9c",
  "target": "006e4b1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006eebac`](#insn-006eebac)

~~~json
{
  "source": "006eebac",
  "target": "006e4b1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006eebb4`](#insn-006eebb4)

~~~json
{
  "source": "006eebb4",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006eebcc`](#insn-006eebcc)

~~~json
{
  "source": "006eebcc",
  "target": "0043a5d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0043a5a9",
  "offset": 47,
  "size": 259,
  "datatype": "byte[259]",
  "bytes": "442d440ea0015c0c1d609302940495069608970a980c990e9a109b149e169d18",
  "capture_start": "0043a5a9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006eebec`](#insn-006eebec)

~~~json
{
  "source": "006eebec",
  "target": "006eec00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eebf4`](#insn-006eebf4)

~~~json
{
  "source": "006eebf4",
  "target": "006eec40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eebfc`](#insn-006eebfc)

~~~json
{
  "source": "006eebfc",
  "target": "006eec64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eec0c`](#insn-006eec0c)

~~~json
{
  "source": "006eec0c",
  "target": "006e4b1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006eec1c`](#insn-006eec1c)

~~~json
{
  "source": "006eec1c",
  "target": "006e4b1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006eec2c`](#insn-006eec2c)

~~~json
{
  "source": "006eec2c",
  "target": "006e4b1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006eec34`](#insn-006eec34)

~~~json
{
  "source": "006eec34",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006eec3c`](#insn-006eec3c)

~~~json
{
  "source": "006eec3c",
  "target": "006eec88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eec40`](#insn-006eec40)

~~~json
{
  "source": "006eec40",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eec68`](#insn-006eec68)

~~~json
{
  "source": "006eec68",
  "target": "Stack[-0x64]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eec70`](#insn-006eec70)

~~~json
{
  "source": "006eec70",
  "target": "006eece0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eec80`](#insn-006eec80)

~~~json
{
  "source": "006eec80",
  "target": "006eeb80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eec84`](#insn-006eec84)

~~~json
{
  "source": "006eec84",
  "target": "006eecdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eec94`](#insn-006eec94)

~~~json
{
  "source": "006eec94",
  "target": "006eec68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eecb0`](#insn-006eecb0)

~~~json
{
  "source": "006eecb0",
  "target": "0043a5d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0043a5a9",
  "offset": 47,
  "size": 259,
  "datatype": "byte[259]",
  "bytes": "442d440ea0015c0c1d609302940495069608970a980c990e9a109b149e169d18",
  "capture_start": "0043a5a9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006eecc8`](#insn-006eecc8)

~~~json
{
  "source": "006eecc8",
  "target": "Stack[-0x6c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eecd8`](#insn-006eecd8)

~~~json
{
  "source": "006eecd8",
  "target": "006eec58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eece4`](#insn-006eece4)

~~~json
{
  "source": "006eece4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eece8`](#insn-006eece8)

~~~json
{
  "source": "006eece8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eecec`](#insn-006eecec)

~~~json
{
  "source": "006eecec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eecf0`](#insn-006eecf0)

~~~json
{
  "source": "006eecf0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eecf4`](#insn-006eecf4)

~~~json
{
  "source": "006eecf4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eecf8`](#insn-006eecf8)

~~~json
{
  "source": "006eecf8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
