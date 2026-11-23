# 00bca2dc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bca214`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca214.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0079.md#compare-a94f2dbf85b3040bc3b5ab8349d76bf3)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bca320`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca320.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-ab9af762a80990b5d61dc6904aac6fbf)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bca2dc",
  "name": "FUN_00bca2dc",
  "size": 436,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0d7c41110f38b6a9273cd5d721c3daf2b7f01d874857b417cd4a458a260e7aee",
  "source_text_sha256": "0d7c41110f38b6a9273cd5d721c3daf2b7f01d874857b417cd4a458a260e7aee",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bca2dc",
        "00bca48f"
      ]
    ],
    "bytes_sha256": "eab844ecb7dbb96b87e836b1d1d1e3efa2f79a7ad0dfae20796a87cf5bdee137",
    "instruction_count": 109,
    "instruction_bytes": 436,
    "body_bytes": 436,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb160](../00bdb/00bdb160.md)
- [00bdd200](../00bdd/00bdd200.md)
- [00bde270](../00bde/00bde270.md)
- [00be10b0](../00be1/00be10b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3277 bytes

~~~c

void FUN_00bca2dc(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  char cVar2;
  char cVar3;
  char cVar4;
  char cVar5;
  undefined1 uVar6;
  bool bVar7;
  int iVar8;
  void *__ptr;
  char cVar9;
  char cVar10;
  undefined1 *puVar11;
  size_t __size;
  long lVar12;
  undefined1 *puVar13;
  char cVar14;
  char cVar15;
  byte *pbVar16;
  size_t __n;
  char local_40 [28];
  undefined4 local_24;
  
  if (7 < *(ulong *)(param_1 + 0x18)) {
    pbVar16 = *(byte **)(param_1 + 0x10);
    cVar9 = '\t';
    cVar2 = cVar9;
    if (0xfffffff5 < *pbVar16 - 0x3a) {
      cVar2 = '\0';
    }
    cVar14 = -0x57;
    cVar3 = -0x57;
    if (0xfffffff5 < pbVar16[1] - 0x3a) {
      cVar3 = -0x30;
    }
    if (0xfffffff5 < pbVar16[2] - 0x3a) {
      cVar9 = '\0';
    }
    if (0xfffffff5 < pbVar16[3] - 0x3a) {
      cVar14 = -0x30;
    }
    cVar10 = '\t';
    cVar4 = cVar10;
    if (0xfffffff5 < pbVar16[4] - 0x3a) {
      cVar4 = '\0';
    }
    cVar15 = -0x57;
    cVar5 = cVar15;
    if (0xfffffff5 < pbVar16[5] - 0x3a) {
      cVar5 = -0x30;
    }
    if (0xfffffff5 < pbVar16[6] - 0x3a) {
      cVar10 = '\0';
    }
    if (0xfffffff5 < pbVar16[7] - 0x3a) {
      cVar15 = -0x30;
    }
    puVar11 = (undefined1 *)((ulong)&local_24 | 1);
    local_24 = (float)CONCAT13(cVar15 + pbVar16[7] + (cVar10 + pbVar16[6]) * '\x10',
                               CONCAT12(cVar5 + pbVar16[5] + (cVar4 + pbVar16[4]) * '\x10',
                                        CONCAT11(cVar14 + pbVar16[3] + (cVar9 + pbVar16[2]) * '\x10'
                                                 ,cVar3 + pbVar16[1] + (cVar2 + *pbVar16) * '\x10'))
                              );
    puVar13 = (undefined1 *)((ulong)&local_24 | 3);
    do {
      uVar6 = puVar11[-1];
      puVar11[-1] = *puVar13;
      *puVar13 = uVar6;
      bVar7 = puVar11 < puVar13 + -1;
      puVar11 = puVar11 + 1;
      puVar13 = puVar13 + -1;
    } while (bVar7);
    local_40[0] = '\0';
    local_40[1] = '\0';
    local_40[2] = '\0';
    local_40[3] = '\0';
    local_40[4] = '\0';
    local_40[5] = '\0';
    local_40[6] = '\0';
    local_40[7] = '\0';
    local_40[8] = '\0';
    local_40[9] = '\0';
    local_40[10] = '\0';
    local_40[0xb] = '\0';
    local_40[0xc] = '\0';
    local_40[0xd] = '\0';
    local_40[0xe] = '\0';
    local_40[0xf] = '\0';
    local_40[0x10] = '\0';
    local_40[0x11] = '\0';
    local_40[0x12] = '\0';
    local_40[0x13] = '\0';
    local_40[0x14] = '\0';
    local_40[0x15] = '\0';
    local_40[0x16] = '\0';
    local_40[0x17] = '\0';
    iVar8 = snprintf(local_40,0x18,"%af",(double)local_24);
    if (iVar8 != 0) {
      lVar12 = param_2[1];
      __n = (size_t)iVar8;
      __ptr = (void *)*param_2;
      if ((ulong)param_2[2] < lVar12 + __n) {
        __size = param_2[2] * 2;
        uVar1 = lVar12 + __n + 0x3e0;
        if (__size < uVar1 || __size - uVar1 == 0) {
          __size = uVar1;
        }
        param_2[2] = __size;
        __ptr = realloc(__ptr,__size);
        *param_2 = __ptr;
        if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
          abort();
        }
        lVar12 = param_2[1];
      }
      memcpy((void *)((long)__ptr + lVar12),local_40,__n);
      param_2[1] = param_2[1] + __n;
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bca2dc"></a> `00bca2dc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bca2e0"></a> `00bca2e0` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bca2e4"></a> `00bca2e4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bca2e8"></a> `00bca2e8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bca2ec"></a> `00bca2ec` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bca2f0"></a> `00bca2f0` | `08 0c 40 f9` | ldr x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bca2f4"></a> `00bca2f4` | `1f 21 00 f1` | cmp x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bca2f8"></a> `00bca2f8` | `03 0c 00 54` | b.cc 0x00bca478 | `CONDITIONAL_JUMP`
<a id="insn-00bca2fc"></a> `00bca2fc` | `0b 08 40 f9` | ldr x11,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bca300"></a> `00bca300` | `28 01 80 52` | mov w8,#0x9 | `FALL_THROUGH`
<a id="insn-00bca304"></a> `00bca304` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bca308"></a> `00bca308` | `e9 05 80 12` | mov w9,#0xffffffd0 | `FALL_THROUGH`
<a id="insn-00bca30c"></a> `00bca30c` | `ca 0a 80 12` | mov w10,#0xffffffa9 | `FALL_THROUGH`
<a id="insn-00bca310"></a> `00bca310` | `6c 01 40 39` | ldrb w12,[x11] | `FALL_THROUGH`
<a id="insn-00bca314"></a> `00bca314` | `6d 05 40 39` | ldrb w13,[x11, #0x1] | `FALL_THROUGH`
<a id="insn-00bca318"></a> `00bca318` | `6e 09 40 39` | ldrb w14,[x11, #0x2] | `FALL_THROUGH`
<a id="insn-00bca31c"></a> `00bca31c` | `6f 0d 40 39` | ldrb w15,[x11, #0x3] | `FALL_THROUGH`
<a id="insn-00bca320"></a> `00bca320` | `71 11 40 39` | ldrb w17,[x11, #0x4] | `FALL_THROUGH`
<a id="insn-00bca324"></a> `00bca324` | `90 e9 00 51` | sub w16,w12,#0x3a | `FALL_THROUGH`
<a id="insn-00bca328"></a> `00bca328` | `a0 e9 00 51` | sub w0,w13,#0x3a | `FALL_THROUGH`
<a id="insn-00bca32c"></a> `00bca32c` | `1f 2a 00 31` | cmn w16,#0xa | `FALL_THROUGH`
<a id="insn-00bca330"></a> `00bca330` | `70 15 40 39` | ldrb w16,[x11, #0x5] | `FALL_THROUGH`
<a id="insn-00bca334"></a> `00bca334` | `01 31 9f 1a` | csel w1,w8,wzr,cc | `FALL_THROUGH`
<a id="insn-00bca338"></a> `00bca338` | `1f 28 00 31` | cmn w0,#0xa | `FALL_THROUGH`
<a id="insn-00bca33c"></a> `00bca33c` | `c0 e9 00 51` | sub w0,w14,#0x3a | `FALL_THROUGH`
<a id="insn-00bca340"></a> `00bca340` | `2c 00 0c 0b` | add w12,w1,w12 | `FALL_THROUGH`
<a id="insn-00bca344"></a> `00bca344` | `41 31 89 1a` | csel w1,w10,w9,cc | `FALL_THROUGH`
<a id="insn-00bca348"></a> `00bca348` | `1f 28 00 31` | cmn w0,#0xa | `FALL_THROUGH`
<a id="insn-00bca34c"></a> `00bca34c` | `e0 e9 00 51` | sub w0,w15,#0x3a | `FALL_THROUGH`
<a id="insn-00bca350"></a> `00bca350` | `2d 00 0d 0b` | add w13,w1,w13 | `FALL_THROUGH`
<a id="insn-00bca354"></a> `00bca354` | `01 31 9f 1a` | csel w1,w8,wzr,cc | `FALL_THROUGH`
<a id="insn-00bca358"></a> `00bca358` | `1f 28 00 31` | cmn w0,#0xa | `FALL_THROUGH`
<a id="insn-00bca35c"></a> `00bca35c` | `60 19 40 39` | ldrb w0,[x11, #0x6] | `FALL_THROUGH`
<a id="insn-00bca360"></a> `00bca360` | `ac 11 0c 0b` | add w12,w13,w12, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00bca364"></a> `00bca364` | `2d ea 00 51` | sub w13,w17,#0x3a | `FALL_THROUGH`
<a id="insn-00bca368"></a> `00bca368` | `6b 1d 40 39` | ldrb w11,[x11, #0x7] | `FALL_THROUGH`
<a id="insn-00bca36c"></a> `00bca36c` | `2e 00 0e 0b` | add w14,w1,w14 | `FALL_THROUGH`
<a id="insn-00bca370"></a> `00bca370` | `41 31 89 1a` | csel w1,w10,w9,cc | `FALL_THROUGH`
<a id="insn-00bca374"></a> `00bca374` | `bf 29 00 31` | cmn w13,#0xa | `FALL_THROUGH`
<a id="insn-00bca378"></a> `00bca378` | `0d ea 00 51` | sub w13,w16,#0x3a | `FALL_THROUGH`
<a id="insn-00bca37c"></a> `00bca37c` | `2f 00 0f 0b` | add w15,w1,w15 | `FALL_THROUGH`
<a id="insn-00bca380"></a> `00bca380` | `01 31 9f 1a` | csel w1,w8,wzr,cc | `FALL_THROUGH`
<a id="insn-00bca384"></a> `00bca384` | `bf 29 00 31` | cmn w13,#0xa | `FALL_THROUGH`
<a id="insn-00bca388"></a> `00bca388` | `0d e8 00 51` | sub w13,w0,#0x3a | `FALL_THROUGH`
<a id="insn-00bca38c"></a> `00bca38c` | `ac c3 1f 38` | sturb w12,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bca390"></a> `00bca390` | `4c 31 89 1a` | csel w12,w10,w9,cc | `FALL_THROUGH`
<a id="insn-00bca394"></a> `00bca394` | `bf 29 00 31` | cmn w13,#0xa | `FALL_THROUGH`
<a id="insn-00bca398"></a> `00bca398` | `6d e9 00 51` | sub w13,w11,#0x3a | `FALL_THROUGH`
<a id="insn-00bca39c"></a> `00bca39c` | `8c 01 10 0b` | add w12,w12,w16 | `FALL_THROUGH`
<a id="insn-00bca3a0"></a> `00bca3a0` | `08 31 9f 1a` | csel w8,w8,wzr,cc | `FALL_THROUGH`
<a id="insn-00bca3a4"></a> `00bca3a4` | `bf 29 00 31` | cmn w13,#0xa | `FALL_THROUGH`
<a id="insn-00bca3a8"></a> `00bca3a8` | `2d 00 11 0b` | add w13,w1,w17 | `FALL_THROUGH`
<a id="insn-00bca3ac"></a> `00bca3ac` | `49 31 89 1a` | csel w9,w10,w9,cc | `FALL_THROUGH`
<a id="insn-00bca3b0"></a> `00bca3b0` | `08 01 00 0b` | add w8,w8,w0 | `FALL_THROUGH`
<a id="insn-00bca3b4"></a> `00bca3b4` | `ee 11 0e 0b` | add w14,w15,w14, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00bca3b8"></a> `00bca3b8` | `29 01 0b 0b` | add w9,w9,w11 | `FALL_THROUGH`
<a id="insn-00bca3bc"></a> `00bca3bc` | `8a 11 0d 0b` | add w10,w12,w13, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00bca3c0"></a> `00bca3c0` | `2b 11 08 0b` | add w11,w9,w8, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00bca3c4"></a> `00bca3c4` | `a9 13 00 d1` | sub x9,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00bca3c8"></a> `00bca3c8` | `ae d3 1f 38` | sturb w14,[x29, #-0x3] | `FALL_THROUGH`
<a id="insn-00bca3cc"></a> `00bca3cc` | `28 01 40 b2` | orr x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bca3d0"></a> `00bca3d0` | `29 05 40 b2` | orr x9,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00bca3d4"></a> `00bca3d4` | `aa e3 1f 38` | sturb w10,[x29, #-0x2] | `FALL_THROUGH`
<a id="insn-00bca3d8"></a> `00bca3d8` | `ab f3 1f 38` | sturb w11,[x29, #-0x1] | `FALL_THROUGH`
<a id="insn-00bca3dc"></a> `00bca3dc` | `2a 01 40 39` | ldrb w10,[x9] | `FALL_THROUGH`
<a id="insn-00bca3e0"></a> `00bca3e0` | `0b f1 5f 38` | ldurb w11,[x8, #-0x1] | `FALL_THROUGH`
<a id="insn-00bca3e4"></a> `00bca3e4` | `0a f1 1f 38` | sturb w10,[x8, #-0x1] | `FALL_THROUGH`
<a id="insn-00bca3e8"></a> `00bca3e8` | `2b f5 1f 38` | strb w11,[x9], #-0x1 | `FALL_THROUGH`
<a id="insn-00bca3ec"></a> `00bca3ec` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bca3f0"></a> `00bca3f0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bca3f4"></a> `00bca3f4` | `43 ff ff 54` | b.cc 0x00bca3dc | `CONDITIONAL_JUMP`
<a id="insn-00bca3f8"></a> `00bca3f8` | `a0 c3 5f bc` | ldur s0,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bca3fc"></a> `00bca3fc` | `e2 b6 ff d0` | adrp x2,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bca400"></a> `00bca400` | `42 10 00 91` | add x2,x2,#0x4 | `FALL_THROUGH`
<a id="insn-00bca404"></a> `00bca404` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bca408"></a> `00bca408` | `01 03 80 52` | mov w1,#0x18 | `FALL_THROUGH`
<a id="insn-00bca40c"></a> `00bca40c` | `ff 7f 00 a9` | stp xzr,xzr,[sp] | `FALL_THROUGH`
<a id="insn-00bca410"></a> `00bca410` | `00 c0 22 1e` | fcvt d0,s0 | `FALL_THROUGH`
<a id="insn-00bca414"></a> `00bca414` | `ff 0b 00 f9` | str xzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bca418"></a> `00bca418` | `26 5b 00 94` | bl 0x00be10b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bca41c"></a> `00bca41c` | `e0 02 00 34` | cbz w0,0x00bca478 | `CONDITIONAL_JUMP`
<a id="insn-00bca420"></a> `00bca420` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bca424"></a> `00bca424` | `14 7c 40 93` | sxtw x20,w0 | `FALL_THROUGH`
<a id="insn-00bca428"></a> `00bca428` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bca42c"></a> `00bca42c` | `0a 01 14 8b` | add x10,x8,x20 | `FALL_THROUGH`
<a id="insn-00bca430"></a> `00bca430` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bca434"></a> `00bca434` | `49 01 00 54` | b.ls 0x00bca45c | `CONDITIONAL_JUMP`
<a id="insn-00bca438"></a> `00bca438` | `28 f9 7f d3` | lsl x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bca43c"></a> `00bca43c` | `49 81 0f 91` | add x9,x10,#0x3e0 | `FALL_THROUGH`
<a id="insn-00bca440"></a> `00bca440` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bca444"></a> `00bca444` | `01 81 89 9a` | csel x1,x8,x9,hi | `FALL_THROUGH`
<a id="insn-00bca448"></a> `00bca448` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bca44c"></a> `00bca44c` | `6d 4b 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bca450"></a> `00bca450` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bca454"></a> `00bca454` | `c0 01 00 b4` | cbz x0,0x00bca48c | `CONDITIONAL_JUMP`
<a id="insn-00bca458"></a> `00bca458` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bca45c"></a> `00bca45c` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00bca460"></a> `00bca460` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bca464"></a> `00bca464` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00bca468"></a> `00bca468` | `3e 43 00 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00bca46c"></a> `00bca46c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bca470"></a> `00bca470` | `08 01 14 8b` | add x8,x8,x20 | `FALL_THROUGH`
<a id="insn-00bca474"></a> `00bca474` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bca478"></a> `00bca478` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bca47c"></a> `00bca47c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bca480"></a> `00bca480` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bca484"></a> `00bca484` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bca488"></a> `00bca488` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bca48c"></a> `00bca48c` | `79 4f 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bca2dc`](#insn-00bca2dc) 範囲 `[['00bca2dc', '00bca2fb']]`
  - `CONDITIONAL_JUMP` [`00bca2f8`](#insn-00bca2f8) → [`00bca478`](#insn-00bca478)
  - `FALL_THROUGH` [`00bca2f8`](#insn-00bca2f8) → [`00bca2fc`](#insn-00bca2fc)
- ブロック [`00bca2fc`](#insn-00bca2fc) 範囲 `[['00bca2fc', '00bca3db']]`
  - `FALL_THROUGH` [`00bca3d8`](#insn-00bca3d8) → [`00bca3dc`](#insn-00bca3dc)
- ブロック [`00bca3dc`](#insn-00bca3dc) 範囲 `[['00bca3dc', '00bca3f7']]`
  - `CONDITIONAL_JUMP` [`00bca3f4`](#insn-00bca3f4) → [`00bca3dc`](#insn-00bca3dc)
  - `FALL_THROUGH` [`00bca3f4`](#insn-00bca3f4) → [`00bca3f8`](#insn-00bca3f8)
- ブロック [`00bca3f8`](#insn-00bca3f8) 範囲 `[['00bca3f8', '00bca41f']]`
  - `CONDITIONAL_JUMP` [`00bca41c`](#insn-00bca41c) → [`00bca478`](#insn-00bca478)
  - `FALL_THROUGH` [`00bca41c`](#insn-00bca41c) → [`00bca420`](#insn-00bca420)
- ブロック [`00bca420`](#insn-00bca420) 範囲 `[['00bca420', '00bca437']]`
  - `CONDITIONAL_JUMP` [`00bca434`](#insn-00bca434) → [`00bca45c`](#insn-00bca45c)
  - `FALL_THROUGH` [`00bca434`](#insn-00bca434) → [`00bca438`](#insn-00bca438)
- ブロック [`00bca438`](#insn-00bca438) 範囲 `[['00bca438', '00bca457']]`
  - `CONDITIONAL_JUMP` [`00bca454`](#insn-00bca454) → [`00bca48c`](#insn-00bca48c)
  - `FALL_THROUGH` [`00bca454`](#insn-00bca454) → [`00bca458`](#insn-00bca458)
- ブロック [`00bca458`](#insn-00bca458) 範囲 `[['00bca458', '00bca45b']]`
  - `FALL_THROUGH` [`00bca458`](#insn-00bca458) → [`00bca45c`](#insn-00bca45c)
- ブロック [`00bca45c`](#insn-00bca45c) 範囲 `[['00bca45c', '00bca477']]`
  - `FALL_THROUGH` [`00bca474`](#insn-00bca474) → [`00bca478`](#insn-00bca478)
- ブロック [`00bca478`](#insn-00bca478) 範囲 `[['00bca478', '00bca48b']]`
- ブロック [`00bca48c`](#insn-00bca48c) 範囲 `[['00bca48c', '00bca48f']]`

## 命令位置別の参照

- [`00bca2e4`](#insn-00bca2e4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca2e8`](#insn-00bca2e8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca2f8`](#insn-00bca2f8) → [`00bca478`](#insn-00bca478) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca38c`](#insn-00bca38c) → `Stack[-0x24]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca3c8`](#insn-00bca3c8) → `Stack[-0x23]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca3d4`](#insn-00bca3d4) → `Stack[-0x22]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca3d8`](#insn-00bca3d8) → `Stack[-0x21]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca3f4`](#insn-00bca3f4) → [`00bca3dc`](#insn-00bca3dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca3f8`](#insn-00bca3f8) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca400`](#insn-00bca400) → `002a8004`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca40c`](#insn-00bca40c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca414`](#insn-00bca414) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca418`](#insn-00bca418) → [`00be10b0`](../00be1/00be10b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be10b0` · 推定シンボル `None` · 推定型 `None`
- [`00bca41c`](#insn-00bca41c) → [`00bca478`](#insn-00bca478) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca434`](#insn-00bca434) → [`00bca45c`](#insn-00bca45c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca44c`](#insn-00bca44c) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bca454`](#insn-00bca454) → [`00bca48c`](#insn-00bca48c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca468`](#insn-00bca468) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00bca478`](#insn-00bca478) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca47c`](#insn-00bca47c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca48c`](#insn-00bca48c) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bca2e4`](#insn-00bca2e4)

~~~json
{
  "source": "00bca2e4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca2e8`](#insn-00bca2e8)

~~~json
{
  "source": "00bca2e8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca2f8`](#insn-00bca2f8)

~~~json
{
  "source": "00bca2f8",
  "target": "00bca478",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca38c`](#insn-00bca38c)

~~~json
{
  "source": "00bca38c",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca3c8`](#insn-00bca3c8)

~~~json
{
  "source": "00bca3c8",
  "target": "Stack[-0x23]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca3d4`](#insn-00bca3d4)

~~~json
{
  "source": "00bca3d4",
  "target": "Stack[-0x22]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca3d8`](#insn-00bca3d8)

~~~json
{
  "source": "00bca3d8",
  "target": "Stack[-0x21]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca3f4`](#insn-00bca3f4)

~~~json
{
  "source": "00bca3f4",
  "target": "00bca3dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca3f8`](#insn-00bca3f8)

~~~json
{
  "source": "00bca3f8",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca400`](#insn-00bca400)

~~~json
{
  "source": "00bca400",
  "target": "002a8004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca40c`](#insn-00bca40c)

~~~json
{
  "source": "00bca40c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca414`](#insn-00bca414)

~~~json
{
  "source": "00bca414",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca418`](#insn-00bca418)

~~~json
{
  "source": "00bca418",
  "target": "00be10b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca41c`](#insn-00bca41c)

~~~json
{
  "source": "00bca41c",
  "target": "00bca478",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca434`](#insn-00bca434)

~~~json
{
  "source": "00bca434",
  "target": "00bca45c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca44c`](#insn-00bca44c)

~~~json
{
  "source": "00bca44c",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca454`](#insn-00bca454)

~~~json
{
  "source": "00bca454",
  "target": "00bca48c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca468`](#insn-00bca468)

~~~json
{
  "source": "00bca468",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca478`](#insn-00bca478)

~~~json
{
  "source": "00bca478",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca47c`](#insn-00bca47c)

~~~json
{
  "source": "00bca47c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca48c`](#insn-00bca48c)

~~~json
{
  "source": "00bca48c",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
