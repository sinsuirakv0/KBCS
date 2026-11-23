# 00afeae0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afea18`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afea18.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-f63614790689f80106ff974505bfcb7a)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afeb24`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afeb24.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0066.md#compare-699429eaa48bb1e343105928db6fc3cb)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afeae0",
  "name": "_ZN8firebase26ReferenceCountedFutureImplD1Ev",
  "size": 504,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3c683f8f1fb4d7e6fdee4783b080d152c8f1f89f98e2334e3fe685316f86e09d",
  "source_text_sha256": "3c683f8f1fb4d7e6fdee4783b080d152c8f1f89f98e2334e3fe685316f86e09d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afeae0",
        "00afecd7"
      ]
    ],
    "bytes_sha256": "3ea2c4593f91a3ac17a10a00f914e789bfaf426681759bc625965838e2b8b0b6",
    "instruction_count": 126,
    "instruction_bytes": 504,
    "body_bytes": 504,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00bddda0](../00bdd/00bddda0.md)
- [00bdedd0](../00bde/00bdedd0.md)

## 呼び出し先

- [00b0129c](../00b01/00b0129c.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)
- [00bddc00](../00bdd/00bddc00.md)
- [00bddd80](../00bdd/00bddd80.md)
- [00bdde80](../00bdd/00bdde80.md)
- [00bddf10](../00bdd/00bddf10.md)
- [00bde700](../00bde/00bde700.md)
- [00bde8c0](../00bde/00bde8c0.md)
- [00bded80](../00bde/00bded80.md)

## 関連文字列（未確認候補）

~~~text
"Future with handle %d still exists though its backing API 0x%X is being deleted. Please call Future::Release() before deleting the backing API."
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4313 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImplD1Ev(long *param_1)

{
  long *plVar1;
  long lVar2;
  long *plVar3;
  long *plVar4;
  long lVar5;
  void *pvVar6;
  ulong uVar7;
  void *pvVar8;
  void *pvVar9;
  
  lVar2 = param_1[10];
  *param_1 = (long)(PTR__ZTVN8firebase26ReferenceCountedFutureImplE_00c1b860 + 0x10);
  if (param_1[0xb] != lVar2) {
    lVar5 = 0;
    uVar7 = 0;
    do {
      lVar2 = lVar2 + lVar5;
      _ZN8firebase5Mutex7AcquireEv(lVar2);
      plVar1 = *(long **)(lVar2 + 0x28);
      if (plVar1 != (long *)0x0) {
        (**(code **)(*plVar1 + 0x60))(plVar1,lVar2);
        (**(code **)(**(long **)(lVar2 + 0x28) + 0x18))(*(long **)(lVar2 + 0x28),lVar2 + 0x30);
        *(undefined8 *)(lVar2 + 0x28) = 0;
      }
      _ZN8firebase5Mutex7ReleaseEv(lVar2);
      lVar2 = param_1[10];
      uVar7 = uVar7 + 1;
      lVar5 = lVar5 + 0x40;
    } while (uVar7 < (ulong)(param_1[0xb] - lVar2 >> 6));
  }
                    /* catch() { ... } // from try @ 00afdd08 with catch @ 00afeb88 */
  _ZN8firebase15CleanupNotifier10CleanupAllEv(param_1 + 0xd);
  _ZN8firebase15CleanupNotifier10CleanupAllEv(param_1 + 0x19);
  plVar1 = param_1 + 6;
  lVar2 = param_1[8];
  while (lVar2 != 0) {
    pvVar9 = (void *)*plVar1;
    _ZN8firebase10LogWarningEPKcz
              ("Future with handle %d still exists though its backing API 0x%X is being deleted. Please call Future::Release() before deleting the backing API."
               ,*(undefined8 *)((long)pvVar9 + 0x20),(ulong)param_1 & 0xffffffff);
    pvVar8 = *(void **)((long)pvVar9 + 0x28);
    plVar4 = *(long **)((long)pvVar9 + 8);
    if (*(long **)((long)pvVar9 + 8) == (long *)0x0) {
      plVar4 = (long *)((long)pvVar9 + 0x10);
      plVar3 = (long *)*plVar4;
      if ((void *)*plVar3 != pvVar9) {
        do {
          lVar2 = *plVar4;
                    /* catch() { ... } // from try @ 00afdce8 with catch @ 00afec04 */
          plVar4 = (long *)(lVar2 + 0x10);
          plVar3 = (long *)*plVar4;
        } while (*plVar3 != lVar2);
      }
    }
    else {
      do {
        plVar3 = plVar4;
                    /* catch() { ... } // from try @ 00afdcfc with catch @ 00afebe4 */
        plVar4 = (long *)*plVar3;
      } while ((long *)*plVar3 != (long *)0x0);
    }
    if ((void *)*plVar1 == pvVar9) {
      *plVar1 = (long)plVar3;
    }
    param_1[8] = param_1[8] + -1;
    _ZNSt6__ndk113__tree_removeIPNS_16__tree_node_baseIPvEEEEvT_S5_(param_1[7],pvVar9);
    _ZdlPv(pvVar9);
    if (pvVar8 != (void *)0x0) {
      _ZN8firebase17FutureBackingDataD1Ev(pvVar8);
      _ZdlPv(pvVar8);
    }
    lVar2 = param_1[8];
  }
  _ZN8firebase15CleanupNotifierD2Ev(param_1 + 0x19);
                    /* catch() { ... } // from try @ 00afdcdc with catch @ 00afec64 */
  _ZN8firebase15CleanupNotifierD2Ev(param_1 + 0xd);
  pvVar8 = (void *)param_1[10];
  if (pvVar8 != (void *)0x0) {
                    /* catch() { ... } // from try @ 00afdccc with catch @ 00afec74 */
    pvVar6 = (void *)param_1[0xb];
    pvVar9 = pvVar8;
    if (pvVar6 != pvVar8) {
      do {
                    /* catch() { ... } // from try @ 00afdcb8 with catch @ 00afec84 */
        pvVar6 = (void *)((long)pvVar6 + -0x40);
        FUN_00b0129c(param_1 + 0xc,pvVar6);
                    /* catch() { ... } // from try @ 00afdcac with catch @ 00afec94 */
      } while (pvVar8 != pvVar6);
      pvVar9 = (void *)param_1[10];
    }
    param_1[0xb] = (long)pvVar8;
    _ZdlPv(pvVar9);
  }
                    /* catch() { ... } // from try @ 00afdc8c with catch @ 00afecb8 */
  _ZNSt6__ndk16__treeINS_12__value_typeImPN8firebase17FutureBackingDataEEENS_19__map_value_compareImS5_NS_4lessImEELb1EEENS_9allocatorIS5_EEE7destroyEPNS_11__tree_nodeIS5_PvEE
            (plVar1,param_1[7]);
                    /* catch() { ... } // from try @ 00afdc7c with catch @ 00afecbc */
                    /* catch() { ... } // from try @ 00afdc64 with catch @ 00afecc4 */
                    /* catch() { ... } // from try @ 00afdc60 with catch @ 00afecc8 */
                    /* catch() { ... } // from try @ 00afdbc0 with catch @ 00afeccc */
                    /* catch() { ... } // from try @ 00afdbb0 with catch @ 00afecd0 */
                    /* catch() { ... } // from try @ 00afdb40 with catch @ 00afecd4 */
  _ZN8firebase5MutexD1Ev(param_1 + 1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afeae0"></a> `00afeae0` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00afeae4"></a> `00afeae4` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afeae8"></a> `00afeae8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afeaec"></a> `00afeaec` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afeaf0"></a> `00afeaf0` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afeaf4"></a> `00afeaf4` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00afeaf8"></a> `00afeaf8` | `ea 08 00 b0` | adrp x10,0xc1b000 | `FALL_THROUGH`
<a id="insn-00afeafc"></a> `00afeafc` | `08 24 45 a9` | ldp x8,x9,[x0, #0x50] | `FALL_THROUGH`
<a id="insn-00afeb00"></a> `00afeb00` | `4a 31 44 f9` | ldr x10,[x10, #0x860] | `FALL_THROUGH`
<a id="insn-00afeb04"></a> `00afeb04` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afeb08"></a> `00afeb08` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00afeb0c"></a> `00afeb0c` | `4a 41 00 91` | add x10,x10,#0x10 | `FALL_THROUGH`
<a id="insn-00afeb10"></a> `00afeb10` | `0a 00 00 f9` | str x10,[x0] | `FALL_THROUGH`
<a id="insn-00afeb14"></a> `00afeb14` | `80 03 00 54` | b.eq 0x00afeb84 | `CONDITIONAL_JUMP`
<a id="insn-00afeb18"></a> `00afeb18` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00afeb1c"></a> `00afeb1c` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00afeb20"></a> `00afeb20` | `09 00 00 14` | b 0x00afeb44 | `UNCONDITIONAL_JUMP`
<a id="insn-00afeb24"></a> `00afeb24` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afeb28"></a> `00afeb28` | `2e 7c 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00afeb2c"></a> `00afeb2c` | `68 26 45 a9` | ldp x8,x9,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00afeb30"></a> `00afeb30` | `d6 06 00 91` | add x22,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00afeb34"></a> `00afeb34` | `b5 02 01 91` | add x21,x21,#0x40 | `FALL_THROUGH`
<a id="insn-00afeb38"></a> `00afeb38` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00afeb3c"></a> `00afeb3c` | `df 1a 89 eb` | cmp x22,x9, ASR #0x6 | `FALL_THROUGH`
<a id="insn-00afeb40"></a> `00afeb40` | `22 02 00 54` | b.cs 0x00afeb84 | `CONDITIONAL_JUMP`
<a id="insn-00afeb44"></a> `00afeb44` | `14 01 15 8b` | add x20,x8,x21 | `FALL_THROUGH`
<a id="insn-00afeb48"></a> `00afeb48` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afeb4c"></a> `00afeb4c` | `21 7c 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00afeb50"></a> `00afeb50` | `80 16 40 f9` | ldr x0,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00afeb54"></a> `00afeb54` | `80 fe ff b4` | cbz x0,0x00afeb24 | `CONDITIONAL_JUMP`
<a id="insn-00afeb58"></a> `00afeb58` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00afeb5c"></a> `00afeb5c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00afeb60"></a> `00afeb60` | `08 31 40 f9` | ldr x8,[x8, #0x60] | `FALL_THROUGH`
<a id="insn-00afeb64"></a> `00afeb64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afeb68"></a> `00afeb68` | `80 16 40 f9` | ldr x0,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00afeb6c"></a> `00afeb6c` | `81 c2 00 91` | add x1,x20,#0x30 | `FALL_THROUGH`
<a id="insn-00afeb70"></a> `00afeb70` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00afeb74"></a> `00afeb74` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00afeb78"></a> `00afeb78` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afeb7c"></a> `00afeb7c` | `9f 16 00 f9` | str xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00afeb80"></a> `00afeb80` | `e9 ff ff 17` | b 0x00afeb24 | `UNCONDITIONAL_JUMP`
<a id="insn-00afeb84"></a> `00afeb84` | `75 a2 01 91` | add x21,x19,#0x68 | `FALL_THROUGH`
<a id="insn-00afeb88"></a> `00afeb88` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afeb8c"></a> `00afeb8c` | `4d 7f 03 94` | bl 0x00bde8c0 | `UNCONDITIONAL_CALL`
<a id="insn-00afeb90"></a> `00afeb90` | `76 22 03 91` | add x22,x19,#0xc8 | `FALL_THROUGH`
<a id="insn-00afeb94"></a> `00afeb94` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00afeb98"></a> `00afeb98` | `4a 7f 03 94` | bl 0x00bde8c0 | `UNCONDITIONAL_CALL`
<a id="insn-00afeb9c"></a> `00afeb9c` | `68 22 40 f9` | ldr x8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00afeba0"></a> `00afeba0` | `74 c2 00 91` | add x20,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00afeba4"></a> `00afeba4` | `c8 05 00 b4` | cbz x8,0x00afec5c | `CONDITIONAL_JUMP`
<a id="insn-00afeba8"></a> `00afeba8` | `97 bc ff d0` | adrp x23,0x290000 | `FALL_THROUGH`
<a id="insn-00afebac"></a> `00afebac` | `f7 7a 0e 91` | add x23,x23,#0x39e | `FALL_THROUGH`
<a id="insn-00afebb0"></a> `00afebb0` | `03 00 00 14` | b 0x00afebbc | `UNCONDITIONAL_JUMP`
<a id="insn-00afebb4"></a> `00afebb4` | `68 22 40 f9` | ldr x8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00afebb8"></a> `00afebb8` | `28 05 00 b4` | cbz x8,0x00afec5c | `CONDITIONAL_JUMP`
<a id="insn-00afebbc"></a> `00afebbc` | `99 02 40 f9` | ldr x25,[x20] | `FALL_THROUGH`
<a id="insn-00afebc0"></a> `00afebc0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00afebc4"></a> `00afebc4` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00afebc8"></a> `00afebc8` | `21 13 40 f9` | ldr x1,[x25, #0x20] | `FALL_THROUGH`
<a id="insn-00afebcc"></a> `00afebcc` | `d1 7c 03 94` | bl 0x00bddf10 | `UNCONDITIONAL_CALL`
<a id="insn-00afebd0"></a> `00afebd0` | `29 07 40 f9` | ldr x9,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00afebd4"></a> `00afebd4` | `38 17 40 f9` | ldr x24,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00afebd8"></a> `00afebd8` | `a9 00 00 b4` | cbz x9,0x00afebec | `CONDITIONAL_JUMP`
<a id="insn-00afebdc"></a> `00afebdc` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00afebe0"></a> `00afebe0` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00afebe4"></a> `00afebe4` | `c9 ff ff b5` | cbnz x9,0x00afebdc | `CONDITIONAL_JUMP`
<a id="insn-00afebe8"></a> `00afebe8` | `0c 00 00 14` | b 0x00afec18 | `UNCONDITIONAL_JUMP`
<a id="insn-00afebec"></a> `00afebec` | `e9 03 19 aa` | mov x9,x25 | `FALL_THROUGH`
<a id="insn-00afebf0"></a> `00afebf0` | `28 0d 41 f8` | ldr x8,[x9, #0x10]! | `FALL_THROUGH`
<a id="insn-00afebf4"></a> `00afebf4` | `0a 01 40 f9` | ldr x10,[x8] | `FALL_THROUGH`
<a id="insn-00afebf8"></a> `00afebf8` | `5f 01 19 eb` | cmp x10,x25 | `FALL_THROUGH`
<a id="insn-00afebfc"></a> `00afebfc` | `e0 00 00 54` | b.eq 0x00afec18 | `CONDITIONAL_JUMP`
<a id="insn-00afec00"></a> `00afec00` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00afec04"></a> `00afec04` | `e9 03 0a aa` | mov x9,x10 | `FALL_THROUGH`
<a id="insn-00afec08"></a> `00afec08` | `28 0d 41 f8` | ldr x8,[x9, #0x10]! | `FALL_THROUGH`
<a id="insn-00afec0c"></a> `00afec0c` | `0b 01 40 f9` | ldr x11,[x8] | `FALL_THROUGH`
<a id="insn-00afec10"></a> `00afec10` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00afec14"></a> `00afec14` | `61 ff ff 54` | b.ne 0x00afec00 | `CONDITIONAL_JUMP`
<a id="insn-00afec18"></a> `00afec18` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00afec1c"></a> `00afec1c` | `3f 01 19 eb` | cmp x9,x25 | `FALL_THROUGH`
<a id="insn-00afec20"></a> `00afec20` | `41 00 00 54` | b.ne 0x00afec28 | `CONDITIONAL_JUMP`
<a id="insn-00afec24"></a> `00afec24` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00afec28"></a> `00afec28` | `60 a2 43 a9` | ldp x0,x8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00afec2c"></a> `00afec2c` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00afec30"></a> `00afec30` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afec34"></a> `00afec34` | `68 22 00 f9` | str x8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00afec38"></a> `00afec38` | `b2 7e 03 94` | bl 0x00bde700 | `UNCONDITIONAL_CALL`
<a id="insn-00afec3c"></a> `00afec3c` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00afec40"></a> `00afec40` | `f4 70 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00afec44"></a> `00afec44` | `98 fb ff b4` | cbz x24,0x00afebb4 | `CONDITIONAL_JUMP`
<a id="insn-00afec48"></a> `00afec48` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00afec4c"></a> `00afec4c` | `4d 80 03 94` | bl 0x00bded80 | `UNCONDITIONAL_CALL`
<a id="insn-00afec50"></a> `00afec50` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00afec54"></a> `00afec54` | `ef 70 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00afec58"></a> `00afec58` | `d7 ff ff 17` | b 0x00afebb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00afec5c"></a> `00afec5c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00afec60"></a> `00afec60` | `48 7c 03 94` | bl 0x00bddd80 | `UNCONDITIONAL_CALL`
<a id="insn-00afec64"></a> `00afec64` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afec68"></a> `00afec68` | `46 7c 03 94` | bl 0x00bddd80 | `UNCONDITIONAL_CALL`
<a id="insn-00afec6c"></a> `00afec6c` | `77 2a 40 f9` | ldr x23,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00afec70"></a> `00afec70` | `17 02 00 b4` | cbz x23,0x00afecb0 | `CONDITIONAL_JUMP`
<a id="insn-00afec74"></a> `00afec74` | `75 2e 40 f9` | ldr x21,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00afec78"></a> `00afec78` | `bf 02 17 eb` | cmp x21,x23 | `FALL_THROUGH`
<a id="insn-00afec7c"></a> `00afec7c` | `40 01 00 54` | b.eq 0x00afeca4 | `CONDITIONAL_JUMP`
<a id="insn-00afec80"></a> `00afec80` | `76 82 01 91` | add x22,x19,#0x60 | `FALL_THROUGH`
<a id="insn-00afec84"></a> `00afec84` | `b5 02 01 d1` | sub x21,x21,#0x40 | `FALL_THROUGH`
<a id="insn-00afec88"></a> `00afec88` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00afec8c"></a> `00afec8c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00afec90"></a> `00afec90` | `83 09 00 94` | bl 0x00b0129c | `UNCONDITIONAL_CALL`
<a id="insn-00afec94"></a> `00afec94` | `ff 02 15 eb` | cmp x23,x21 | `FALL_THROUGH`
<a id="insn-00afec98"></a> `00afec98` | `61 ff ff 54` | b.ne 0x00afec84 | `CONDITIONAL_JUMP`
<a id="insn-00afec9c"></a> `00afec9c` | `60 2a 40 f9` | ldr x0,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00afeca0"></a> `00afeca0` | `02 00 00 14` | b 0x00afeca8 | `UNCONDITIONAL_JUMP`
<a id="insn-00afeca4"></a> `00afeca4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00afeca8"></a> `00afeca8` | `77 2e 00 f9` | str x23,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00afecac"></a> `00afecac` | `d9 70 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00afecb0"></a> `00afecb0` | `61 1e 40 f9` | ldr x1,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00afecb4"></a> `00afecb4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afecb8"></a> `00afecb8` | `72 7c 03 94` | bl 0x00bdde80 | `UNCONDITIONAL_CALL`
<a id="insn-00afecbc"></a> `00afecbc` | `60 22 00 91` | add x0,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00afecc0"></a> `00afecc0` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afecc4"></a> `00afecc4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afecc8"></a> `00afecc8` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afeccc"></a> `00afeccc` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afecd0"></a> `00afecd0` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00afecd4"></a> `00afecd4` | `cb 7b 03 14` | b 0x00bddc00 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afeae0`](#insn-00afeae0) 範囲 `[['00afeae0', '00afeb17']]`
  - `CONDITIONAL_JUMP` [`00afeb14`](#insn-00afeb14) → [`00afeb84`](#insn-00afeb84)
  - `FALL_THROUGH` [`00afeb14`](#insn-00afeb14) → [`00afeb18`](#insn-00afeb18)
- ブロック [`00afeb18`](#insn-00afeb18) 範囲 `[['00afeb18', '00afeb23']]`
  - `UNCONDITIONAL_JUMP` [`00afeb20`](#insn-00afeb20) → [`00afeb44`](#insn-00afeb44)
- ブロック [`00afeb24`](#insn-00afeb24) 範囲 `[['00afeb24', '00afeb43']]`
  - `CONDITIONAL_JUMP` [`00afeb40`](#insn-00afeb40) → [`00afeb84`](#insn-00afeb84)
  - `FALL_THROUGH` [`00afeb40`](#insn-00afeb40) → [`00afeb44`](#insn-00afeb44)
- ブロック [`00afeb44`](#insn-00afeb44) 範囲 `[['00afeb44', '00afeb57']]`
  - `CONDITIONAL_JUMP` [`00afeb54`](#insn-00afeb54) → [`00afeb24`](#insn-00afeb24)
  - `FALL_THROUGH` [`00afeb54`](#insn-00afeb54) → [`00afeb58`](#insn-00afeb58)
- ブロック [`00afeb58`](#insn-00afeb58) 範囲 `[['00afeb58', '00afeb83']]`
  - `UNCONDITIONAL_JUMP` [`00afeb80`](#insn-00afeb80) → [`00afeb24`](#insn-00afeb24)
- ブロック [`00afeb84`](#insn-00afeb84) 範囲 `[['00afeb84', '00afeb87']]`
  - `FALL_THROUGH` [`00afeb84`](#insn-00afeb84) → [`00afeb88`](#insn-00afeb88)
- ブロック [`00afeb88`](#insn-00afeb88) 範囲 `[['00afeb88', '00afeba7']]`
  - `CONDITIONAL_JUMP` [`00afeba4`](#insn-00afeba4) → [`00afec5c`](#insn-00afec5c)
  - `FALL_THROUGH` [`00afeba4`](#insn-00afeba4) → [`00afeba8`](#insn-00afeba8)
- ブロック [`00afeba8`](#insn-00afeba8) 範囲 `[['00afeba8', '00afebb3']]`
  - `UNCONDITIONAL_JUMP` [`00afebb0`](#insn-00afebb0) → [`00afebbc`](#insn-00afebbc)
- ブロック [`00afebb4`](#insn-00afebb4) 範囲 `[['00afebb4', '00afebbb']]`
  - `CONDITIONAL_JUMP` [`00afebb8`](#insn-00afebb8) → [`00afec5c`](#insn-00afec5c)
  - `FALL_THROUGH` [`00afebb8`](#insn-00afebb8) → [`00afebbc`](#insn-00afebbc)
- ブロック [`00afebbc`](#insn-00afebbc) 範囲 `[['00afebbc', '00afebdb']]`
  - `CONDITIONAL_JUMP` [`00afebd8`](#insn-00afebd8) → [`00afebec`](#insn-00afebec)
  - `FALL_THROUGH` [`00afebd8`](#insn-00afebd8) → [`00afebdc`](#insn-00afebdc)
- ブロック [`00afebdc`](#insn-00afebdc) 範囲 `[['00afebdc', '00afebe3']]`
  - `FALL_THROUGH` [`00afebe0`](#insn-00afebe0) → [`00afebe4`](#insn-00afebe4)
- ブロック [`00afebe4`](#insn-00afebe4) 範囲 `[['00afebe4', '00afebe7']]`
  - `CONDITIONAL_JUMP` [`00afebe4`](#insn-00afebe4) → [`00afebdc`](#insn-00afebdc)
  - `FALL_THROUGH` [`00afebe4`](#insn-00afebe4) → [`00afebe8`](#insn-00afebe8)
- ブロック [`00afebe8`](#insn-00afebe8) 範囲 `[['00afebe8', '00afebeb']]`
  - `UNCONDITIONAL_JUMP` [`00afebe8`](#insn-00afebe8) → [`00afec18`](#insn-00afec18)
- ブロック [`00afebec`](#insn-00afebec) 範囲 `[['00afebec', '00afebff']]`
  - `CONDITIONAL_JUMP` [`00afebfc`](#insn-00afebfc) → [`00afec18`](#insn-00afec18)
  - `FALL_THROUGH` [`00afebfc`](#insn-00afebfc) → [`00afec00`](#insn-00afec00)
- ブロック [`00afec00`](#insn-00afec00) 範囲 `[['00afec00', '00afec03']]`
  - `FALL_THROUGH` [`00afec00`](#insn-00afec00) → [`00afec04`](#insn-00afec04)
- ブロック [`00afec04`](#insn-00afec04) 範囲 `[['00afec04', '00afec17']]`
  - `CONDITIONAL_JUMP` [`00afec14`](#insn-00afec14) → [`00afec00`](#insn-00afec00)
  - `FALL_THROUGH` [`00afec14`](#insn-00afec14) → [`00afec18`](#insn-00afec18)
- ブロック [`00afec18`](#insn-00afec18) 範囲 `[['00afec18', '00afec23']]`
  - `CONDITIONAL_JUMP` [`00afec20`](#insn-00afec20) → [`00afec28`](#insn-00afec28)
  - `FALL_THROUGH` [`00afec20`](#insn-00afec20) → [`00afec24`](#insn-00afec24)
- ブロック [`00afec24`](#insn-00afec24) 範囲 `[['00afec24', '00afec27']]`
  - `FALL_THROUGH` [`00afec24`](#insn-00afec24) → [`00afec28`](#insn-00afec28)
- ブロック [`00afec28`](#insn-00afec28) 範囲 `[['00afec28', '00afec47']]`
  - `CONDITIONAL_JUMP` [`00afec44`](#insn-00afec44) → [`00afebb4`](#insn-00afebb4)
  - `FALL_THROUGH` [`00afec44`](#insn-00afec44) → [`00afec48`](#insn-00afec48)
- ブロック [`00afec48`](#insn-00afec48) 範囲 `[['00afec48', '00afec5b']]`
  - `UNCONDITIONAL_JUMP` [`00afec58`](#insn-00afec58) → [`00afebb4`](#insn-00afebb4)
- ブロック [`00afec5c`](#insn-00afec5c) 範囲 `[['00afec5c', '00afec63']]`
  - `FALL_THROUGH` [`00afec60`](#insn-00afec60) → [`00afec64`](#insn-00afec64)
- ブロック [`00afec64`](#insn-00afec64) 範囲 `[['00afec64', '00afec73']]`
  - `CONDITIONAL_JUMP` [`00afec70`](#insn-00afec70) → [`00afecb0`](#insn-00afecb0)
  - `FALL_THROUGH` [`00afec70`](#insn-00afec70) → [`00afec74`](#insn-00afec74)
- ブロック [`00afec74`](#insn-00afec74) 範囲 `[['00afec74', '00afec7f']]`
  - `CONDITIONAL_JUMP` [`00afec7c`](#insn-00afec7c) → [`00afeca4`](#insn-00afeca4)
  - `FALL_THROUGH` [`00afec7c`](#insn-00afec7c) → [`00afec80`](#insn-00afec80)
- ブロック [`00afec80`](#insn-00afec80) 範囲 `[['00afec80', '00afec83']]`
  - `FALL_THROUGH` [`00afec80`](#insn-00afec80) → [`00afec84`](#insn-00afec84)
- ブロック [`00afec84`](#insn-00afec84) 範囲 `[['00afec84', '00afec93']]`
  - `FALL_THROUGH` [`00afec90`](#insn-00afec90) → [`00afec94`](#insn-00afec94)
- ブロック [`00afec94`](#insn-00afec94) 範囲 `[['00afec94', '00afec9b']]`
  - `CONDITIONAL_JUMP` [`00afec98`](#insn-00afec98) → [`00afec84`](#insn-00afec84)
  - `FALL_THROUGH` [`00afec98`](#insn-00afec98) → [`00afec9c`](#insn-00afec9c)
- ブロック [`00afec9c`](#insn-00afec9c) 範囲 `[['00afec9c', '00afeca3']]`
  - `UNCONDITIONAL_JUMP` [`00afeca0`](#insn-00afeca0) → [`00afeca8`](#insn-00afeca8)
- ブロック [`00afeca4`](#insn-00afeca4) 範囲 `[['00afeca4', '00afeca7']]`
  - `FALL_THROUGH` [`00afeca4`](#insn-00afeca4) → [`00afeca8`](#insn-00afeca8)
- ブロック [`00afeca8`](#insn-00afeca8) 範囲 `[['00afeca8', '00afecaf']]`
  - `FALL_THROUGH` [`00afecac`](#insn-00afecac) → [`00afecb0`](#insn-00afecb0)
- ブロック [`00afecb0`](#insn-00afecb0) 範囲 `[['00afecb0', '00afecb7']]`
  - `FALL_THROUGH` [`00afecb4`](#insn-00afecb4) → [`00afecb8`](#insn-00afecb8)
- ブロック [`00afecb8`](#insn-00afecb8) 範囲 `[['00afecb8', '00afecbb']]`
  - `FALL_THROUGH` [`00afecb8`](#insn-00afecb8) → [`00afecbc`](#insn-00afecbc)
- ブロック [`00afecbc`](#insn-00afecbc) 範囲 `[['00afecbc', '00afecc3']]`
  - `FALL_THROUGH` [`00afecc0`](#insn-00afecc0) → [`00afecc4`](#insn-00afecc4)
- ブロック [`00afecc4`](#insn-00afecc4) 範囲 `[['00afecc4', '00afecc7']]`
  - `FALL_THROUGH` [`00afecc4`](#insn-00afecc4) → [`00afecc8`](#insn-00afecc8)
- ブロック [`00afecc8`](#insn-00afecc8) 範囲 `[['00afecc8', '00afeccb']]`
  - `FALL_THROUGH` [`00afecc8`](#insn-00afecc8) → [`00afeccc`](#insn-00afeccc)
- ブロック [`00afeccc`](#insn-00afeccc) 範囲 `[['00afeccc', '00afeccf']]`
  - `FALL_THROUGH` [`00afeccc`](#insn-00afeccc) → [`00afecd0`](#insn-00afecd0)
- ブロック [`00afecd0`](#insn-00afecd0) 範囲 `[['00afecd0', '00afecd3']]`
  - `FALL_THROUGH` [`00afecd0`](#insn-00afecd0) → [`00afecd4`](#insn-00afecd4)
- ブロック [`00afecd4`](#insn-00afecd4) 範囲 `[['00afecd4', '00afecd7']]`

## 命令位置別の参照

- [`00afeae0`](#insn-00afeae0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeae4`](#insn-00afeae4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeae8`](#insn-00afeae8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeaec`](#insn-00afeaec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeaf0`](#insn-00afeaf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeb00`](#insn-00afeb00) → `00c1b860`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00afeb10`](#insn-00afeb10) → `00c10850`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[120]`
- [`00afeb14`](#insn-00afeb14) → [`00afeb84`](#insn-00afeb84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeb20`](#insn-00afeb20) → [`00afeb44`](#insn-00afeb44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeb28`](#insn-00afeb28) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00afeb40`](#insn-00afeb40) → [`00afeb84`](#insn-00afeb84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeb4c`](#insn-00afeb4c) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00afeb54`](#insn-00afeb54) → [`00afeb24`](#insn-00afeb24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeb80`](#insn-00afeb80) → [`00afeb24`](#insn-00afeb24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeb8c`](#insn-00afeb8c) → [`00bde8c0`](../00bde/00bde8c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde8c0` · 推定シンボル `None` · 推定型 `None`
- [`00afeb98`](#insn-00afeb98) → [`00bde8c0`](../00bde/00bde8c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde8c0` · 推定シンボル `None` · 推定型 `None`
- [`00afeba4`](#insn-00afeba4) → [`00afec5c`](#insn-00afec5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afebb0`](#insn-00afebb0) → [`00afebbc`](#insn-00afebbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afebb8`](#insn-00afebb8) → [`00afec5c`](#insn-00afec5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afebc0`](#insn-00afebc0) → `0029039e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00afebcc`](#insn-00afebcc) → [`00bddf10`](../00bdd/00bddf10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf10` · 推定シンボル `None` · 推定型 `None`
- [`00afebd8`](#insn-00afebd8) → [`00afebec`](#insn-00afebec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afebe4`](#insn-00afebe4) → [`00afebdc`](#insn-00afebdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afebe8`](#insn-00afebe8) → [`00afec18`](#insn-00afec18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afebfc`](#insn-00afebfc) → [`00afec18`](#insn-00afec18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afec14`](#insn-00afec14) → [`00afec00`](#insn-00afec00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afec20`](#insn-00afec20) → [`00afec28`](#insn-00afec28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afec38`](#insn-00afec38) → [`00bde700`](../00bde/00bde700.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde700` · 推定シンボル `None` · 推定型 `None`
- [`00afec40`](#insn-00afec40) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00afec44`](#insn-00afec44) → [`00afebb4`](#insn-00afebb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afec4c`](#insn-00afec4c) → [`00bded80`](../00bde/00bded80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bded80` · 推定シンボル `None` · 推定型 `None`
- [`00afec54`](#insn-00afec54) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00afec58`](#insn-00afec58) → [`00afebb4`](#insn-00afebb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afec60`](#insn-00afec60) → [`00bddd80`](../00bdd/00bddd80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddd80` · 推定シンボル `None` · 推定型 `None`
- [`00afec68`](#insn-00afec68) → [`00bddd80`](../00bdd/00bddd80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddd80` · 推定シンボル `None` · 推定型 `None`
- [`00afec70`](#insn-00afec70) → [`00afecb0`](#insn-00afecb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afec7c`](#insn-00afec7c) → [`00afeca4`](#insn-00afeca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afec90`](#insn-00afec90) → [`00b0129c`](../00b01/00b0129c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b0129c` · 推定シンボル `None` · 推定型 `None`
- [`00afec98`](#insn-00afec98) → [`00afec84`](#insn-00afec84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeca0`](#insn-00afeca0) → [`00afeca8`](#insn-00afeca8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afecac`](#insn-00afecac) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00afecb8`](#insn-00afecb8) → [`00bdde80`](../00bdd/00bdde80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdde80` · 推定シンボル `None` · 推定型 `None`
- [`00afecc0`](#insn-00afecc0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afecc4`](#insn-00afecc4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afecc8`](#insn-00afecc8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeccc`](#insn-00afeccc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afecd4`](#insn-00afecd4) → [`00bddc00`](../00bdd/00bddc00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc00` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afeae0`](#insn-00afeae0)

~~~json
{
  "source": "00afeae0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeae4`](#insn-00afeae4)

~~~json
{
  "source": "00afeae4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeae8`](#insn-00afeae8)

~~~json
{
  "source": "00afeae8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeaec`](#insn-00afeaec)

~~~json
{
  "source": "00afeaec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeaf0`](#insn-00afeaf0)

~~~json
{
  "source": "00afeaf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeb00`](#insn-00afeb00)

~~~json
{
  "source": "00afeb00",
  "target": "00c1b860",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b860",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00afeb10`](#insn-00afeb10)

~~~json
{
  "source": "00afeb10",
  "target": "00c10850",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10840",
  "offset": 16,
  "size": 120,
  "datatype": "undefined1[120]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00afeb14`](#insn-00afeb14)

~~~json
{
  "source": "00afeb14",
  "target": "00afeb84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeb20`](#insn-00afeb20)

~~~json
{
  "source": "00afeb20",
  "target": "00afeb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeb28`](#insn-00afeb28)

~~~json
{
  "source": "00afeb28",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afeb40`](#insn-00afeb40)

~~~json
{
  "source": "00afeb40",
  "target": "00afeb84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeb4c`](#insn-00afeb4c)

~~~json
{
  "source": "00afeb4c",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afeb54`](#insn-00afeb54)

~~~json
{
  "source": "00afeb54",
  "target": "00afeb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeb80`](#insn-00afeb80)

~~~json
{
  "source": "00afeb80",
  "target": "00afeb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeb8c`](#insn-00afeb8c)

~~~json
{
  "source": "00afeb8c",
  "target": "00bde8c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afeb98`](#insn-00afeb98)

~~~json
{
  "source": "00afeb98",
  "target": "00bde8c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afeba4`](#insn-00afeba4)

~~~json
{
  "source": "00afeba4",
  "target": "00afec5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afebb0`](#insn-00afebb0)

~~~json
{
  "source": "00afebb0",
  "target": "00afebbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afebb8`](#insn-00afebb8)

~~~json
{
  "source": "00afebb8",
  "target": "00afec5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afebc0`](#insn-00afebc0)

~~~json
{
  "source": "00afebc0",
  "target": "0029039e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029039e",
  "offset": 0,
  "size": 144,
  "datatype": "string",
  "bytes": "46757475726520776974682068616e646c65202564207374696c6c2065786973",
  "capture_start": "0029039e",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afebcc`](#insn-00afebcc)

~~~json
{
  "source": "00afebcc",
  "target": "00bddf10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afebd8`](#insn-00afebd8)

~~~json
{
  "source": "00afebd8",
  "target": "00afebec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afebe4`](#insn-00afebe4)

~~~json
{
  "source": "00afebe4",
  "target": "00afebdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afebe8`](#insn-00afebe8)

~~~json
{
  "source": "00afebe8",
  "target": "00afec18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afebfc`](#insn-00afebfc)

~~~json
{
  "source": "00afebfc",
  "target": "00afec18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afec14`](#insn-00afec14)

~~~json
{
  "source": "00afec14",
  "target": "00afec00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afec20`](#insn-00afec20)

~~~json
{
  "source": "00afec20",
  "target": "00afec28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afec38`](#insn-00afec38)

~~~json
{
  "source": "00afec38",
  "target": "00bde700",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afec40`](#insn-00afec40)

~~~json
{
  "source": "00afec40",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afec44`](#insn-00afec44)

~~~json
{
  "source": "00afec44",
  "target": "00afebb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afec4c`](#insn-00afec4c)

~~~json
{
  "source": "00afec4c",
  "target": "00bded80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afec54`](#insn-00afec54)

~~~json
{
  "source": "00afec54",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afec58`](#insn-00afec58)

~~~json
{
  "source": "00afec58",
  "target": "00afebb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afec60`](#insn-00afec60)

~~~json
{
  "source": "00afec60",
  "target": "00bddd80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afec68`](#insn-00afec68)

~~~json
{
  "source": "00afec68",
  "target": "00bddd80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afec70`](#insn-00afec70)

~~~json
{
  "source": "00afec70",
  "target": "00afecb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afec7c`](#insn-00afec7c)

~~~json
{
  "source": "00afec7c",
  "target": "00afeca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afec90`](#insn-00afec90)

~~~json
{
  "source": "00afec90",
  "target": "00b0129c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afec98`](#insn-00afec98)

~~~json
{
  "source": "00afec98",
  "target": "00afec84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeca0`](#insn-00afeca0)

~~~json
{
  "source": "00afeca0",
  "target": "00afeca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afecac`](#insn-00afecac)

~~~json
{
  "source": "00afecac",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afecb8`](#insn-00afecb8)

~~~json
{
  "source": "00afecb8",
  "target": "00bdde80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afecc0`](#insn-00afecc0)

~~~json
{
  "source": "00afecc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afecc4`](#insn-00afecc4)

~~~json
{
  "source": "00afecc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afecc8`](#insn-00afecc8)

~~~json
{
  "source": "00afecc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeccc`](#insn-00afeccc)

~~~json
{
  "source": "00afeccc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afecd4`](#insn-00afecd4)

~~~json
{
  "source": "00afecd4",
  "target": "00bddc00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
