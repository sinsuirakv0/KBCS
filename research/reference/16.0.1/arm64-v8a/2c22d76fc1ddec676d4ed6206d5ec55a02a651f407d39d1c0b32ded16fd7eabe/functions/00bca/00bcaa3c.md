# 00bcaa3c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bca614`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca614.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-963ee7b818dfeeae57679d108ab4460d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcaad8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcaad8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-2e8fa686d4da5b664ac9d6bfa2e14a78)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcaa3c",
  "name": "_ZN8firebase4auth4Auth14DeleteInternalEv",
  "size": 548,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fc6090d96254dd8643229441b87124c2bbf599c788676fff8f8ba1b059a8cd5e",
  "source_text_sha256": "fc6090d96254dd8643229441b87124c2bbf599c788676fff8f8ba1b059a8cd5e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcaa3c",
        "00bcac5f"
      ]
    ],
    "bytes_sha256": "2e1c59015da97da47db6970ad2f4e83af26834382a26514bb96dd573794ba0ce",
    "instruction_count": 137,
    "instruction_bytes": 548,
    "body_bytes": 548,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5da30](../00c5d/00c5da30.md)

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5aa10](../00c5a/00c5aa10.md)
- [00c5abf0](../00c5a/00c5abf0.md)
- [00c5ac10](../00c5a/00c5ac10.md)
- [00c5b130](../00c5b/00c5b130.md)
- [00c5b5d0](../00c5b/00c5b5d0.md)
- [00c5bce0](../00c5b/00c5bce0.md)
- [00c5da20](../00c5d/00c5da20.md)
- [00c5da50](../00c5d/00c5da50.md)
- [00c5da60](../00c5d/00c5da60.md)
- [00c5da70](../00c5d/00c5da70.md)
- [00c5dab0](../00c5d/00c5dab0.md)
- [00c5db20](../00c5d/00c5db20.md)

## 関連文字列（未確認候補）

~~~text
"Deleting Auth %p for App %p"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3698 bytes

~~~c

void _ZN8firebase4auth4Auth14DeleteInternalEv(long *param_1)

{
  undefined *puVar1;
  ulong uVar2;
  undefined8 uVar3;
  long lVar4;
  long *plVar5;
  long *plVar6;
  undefined8 uVar7;
  long *__ptr;
  long lVar8;
  void *__ptr_00;
  
  uVar7 = *(undefined8 *)PTR__ZN8firebase4auth13g_auths_mutexE_00c9b9a0;
  _ZN8firebase5Mutex7AcquireEv(uVar7);
  if (*param_1 != 0) {
    lVar4 = *param_1 + 0x2e8;
    _ZN8firebase5Mutex7AcquireEv(lVar4);
    *(undefined1 *)(*param_1 + 0x2e4) = 1;
    _ZN8firebase5Mutex7ReleaseEv(lVar4);
    while (uVar2 = _ZNK8firebase26ReferenceCountedFutureImpl14IsSafeToDeleteEv(*param_1 + 0x10),
          (uVar2 & 1) == 0) {
      usleep(100000);
    }
    uVar3 = _ZN8firebase15CleanupNotifier11FindByOwnerEPv(*(undefined8 *)*param_1);
    _ZN8firebase15CleanupNotifier16UnregisterObjectEPv(uVar3,param_1);
    puVar1 = PTR__ZN8firebase4auth7g_authsE_00c9b9a8;
    if (*(long **)PTR__ZN8firebase4auth7g_authsE_00c9b9a8 !=
        (long *)(PTR__ZN8firebase4auth7g_authsE_00c9b9a8 + 8)) {
      __ptr = *(long **)PTR__ZN8firebase4auth7g_authsE_00c9b9a8;
LAB_00bcaaec:
      if ((long *)__ptr[5] != param_1) goto code_r0x00bcaaf8;
      _ZN8firebase8LogDebugEPKcz("Deleting Auth %p for App %p",param_1,__ptr[4]);
      plVar5 = (long *)__ptr[1];
      if ((long *)__ptr[1] == (long *)0x0) {
        plVar5 = __ptr + 2;
        plVar6 = (long *)*plVar5;
        if ((long *)*plVar6 != __ptr) {
          do {
            lVar4 = *plVar5;
            plVar5 = (long *)(lVar4 + 0x10);
            plVar6 = (long *)*plVar5;
          } while (*plVar6 != lVar4);
        }
      }
      else {
        do {
          plVar6 = plVar5;
          plVar5 = (long *)*plVar6;
        } while ((long *)*plVar6 != (long *)0x0);
      }
      if (*(long **)puVar1 == __ptr) {
        *(long **)puVar1 = plVar6;
      }
      *(long *)(puVar1 + 0x10) = *(long *)(puVar1 + 0x10) + -1;
      _ZNSt6__ndk113__tree_removeIPNS_16__tree_node_baseIPvEEEEvT_S5_
                (*(undefined8 *)(puVar1 + 8),__ptr);
      _ZdlPv(__ptr);
    }
LAB_00bcabc4:
    lVar8 = *param_1;
    uVar3 = *(undefined8 *)(puVar1 + 0x10);
    lVar4 = *(long *)(lVar8 + 0x238);
    if (*(long *)(lVar8 + 0x230) != lVar4) {
      do {
        _ZN8firebase4auth4Auth23RemoveAuthStateListenerEPNS0_17AuthStateListenerE
                  (*(undefined8 *)(lVar8 + 8),*(undefined8 *)(lVar4 + -8));
        lVar4 = *(long *)(lVar8 + 0x238);
      } while (*(long *)(lVar8 + 0x230) != lVar4);
    }
    while (*(long *)(lVar8 + 0x248) != *(long *)(lVar8 + 0x250)) {
      _ZN8firebase4auth4Auth21RemoveIdTokenListenerEPNS0_15IdTokenListenerE
                (*(undefined8 *)(lVar8 + 8),*(undefined8 *)(*(long *)(lVar8 + 0x250) + -8));
    }
    if ((int)uVar3 == 0) {
      _ZN8firebase4auth27CleanupCredentialFutureImplEv();
    }
    _ZN8firebase4auth4Auth19DestroyPlatformAuthEPNS0_8AuthDataE(param_1,*param_1);
    __ptr_00 = (void *)*param_1;
    if (__ptr_00 != (void *)0x0) {
      _ZN8firebase4auth8AuthDataD2Ev(__ptr_00);
      _ZdlPv(__ptr_00);
    }
    *param_1 = 0;
  }
  _ZN8firebase5Mutex7ReleaseEv(uVar7);
  return;
code_r0x00bcaaf8:
  plVar5 = (long *)__ptr[1];
  if ((long *)__ptr[1] == (long *)0x0) {
    plVar5 = __ptr + 2;
    plVar6 = (long *)*plVar5;
    if ((long *)*plVar6 != __ptr) {
      do {
        lVar4 = *plVar5;
        plVar5 = (long *)(lVar4 + 0x10);
        plVar6 = (long *)*plVar5;
      } while (*plVar6 != lVar4);
    }
  }
  else {
    do {
      plVar6 = plVar5;
      plVar5 = (long *)*plVar6;
    } while ((long *)*plVar6 != (long *)0x0);
  }
  __ptr = plVar6;
  if (plVar6 == (long *)(PTR__ZN8firebase4auth7g_authsE_00c9b9a8 + 8)) goto LAB_00bcabc4;
  goto LAB_00bcaaec;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcaa3c"></a> `00bcaa3c` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcaa40"></a> `00bcaa40` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcaa44"></a> `00bcaa44` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcaa48"></a> `00bcaa48` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcaa4c"></a> `00bcaa4c` | `88 06 00 b0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcaa50"></a> `00bcaa50` | `08 d1 44 f9` | ldr x8,[x8, #0x9a0] | `FALL_THROUGH`
<a id="insn-00bcaa54"></a> `00bcaa54` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcaa58"></a> `00bcaa58` | `13 01 40 f9` | ldr x19,[x8] | `FALL_THROUGH`
<a id="insn-00bcaa5c"></a> `00bcaa5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcaa60"></a> `00bcaa60` | `e8 3f 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcaa64"></a> `00bcaa64` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcaa68"></a> `00bcaa68` | `08 0f 00 b4` | cbz x8,0x00bcac48 | `CONDITIONAL_JUMP`
<a id="insn-00bcaa6c"></a> `00bcaa6c` | `15 a1 0b 91` | add x21,x8,#0x2e8 | `FALL_THROUGH`
<a id="insn-00bcaa70"></a> `00bcaa70` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcaa74"></a> `00bcaa74` | `e3 3f 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcaa78"></a> `00bcaa78` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcaa7c"></a> `00bcaa7c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcaa80"></a> `00bcaa80` | `09 91 0b 39` | strb w9,[x8, #0x2e4] | `FALL_THROUGH`
<a id="insn-00bcaa84"></a> `00bcaa84` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcaa88"></a> `00bcaa88` | `e2 3f 02 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcaa8c"></a> `00bcaa8c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcaa90"></a> `00bcaa90` | `00 41 00 91` | add x0,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bcaa94"></a> `00bcaa94` | `93 44 02 94` | bl 0x00c5bce0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcaa98"></a> `00bcaa98` | `a0 00 00 37` | tbnz w0,#0x0,0x00bcaaac | `CONDITIONAL_JUMP`
<a id="insn-00bcaa9c"></a> `00bcaa9c` | `00 d4 90 52` | mov w0,#0x86a0 | `FALL_THROUGH`
<a id="insn-00bcaaa0"></a> `00bcaaa0` | `20 00 a0 72` | movk w0,#0x1, LSL #16 | `FALL_THROUGH`
<a id="insn-00bcaaa4"></a> `00bcaaa4` | `1f 4c 02 94` | bl 0x00c5db20 | `UNCONDITIONAL_CALL`
<a id="insn-00bcaaa8"></a> `00bcaaa8` | `f9 ff ff 17` | b 0x00bcaa8c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcaaac"></a> `00bcaaac` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcaab0"></a> `00bcaab0` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bcaab4"></a> `00bcaab4` | `4f 40 02 94` | bl 0x00c5abf0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcaab8"></a> `00bcaab8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcaabc"></a> `00bcaabc` | `55 40 02 94` | bl 0x00c5ac10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcaac0"></a> `00bcaac0` | `96 06 00 b0` | adrp x22,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcaac4"></a> `00bcaac4` | `d6 d6 44 f9` | ldr x22,[x22, #0x9a8] | `FALL_THROUGH`
<a id="insn-00bcaac8"></a> `00bcaac8` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bcaacc"></a> `00bcaacc` | `15 85 40 f8` | ldr x21,[x8], #0x8 | `FALL_THROUGH`
<a id="insn-00bcaad0"></a> `00bcaad0` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00bcaad4"></a> `00bcaad4` | `80 07 00 54` | b.eq 0x00bcabc4 | `CONDITIONAL_JUMP`
<a id="insn-00bcaad8"></a> `00bcaad8` | `c8 22 00 91` | add x8,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00bcaadc"></a> `00bcaadc` | `04 00 00 14` | b 0x00bcaaec | `UNCONDITIONAL_JUMP`
<a id="insn-00bcaae0"></a> `00bcaae0` | `f5 03 0a aa` | mov x21,x10 | `FALL_THROUGH`
<a id="insn-00bcaae4"></a> `00bcaae4` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00bcaae8"></a> `00bcaae8` | `e0 06 00 54` | b.eq 0x00bcabc4 | `CONDITIONAL_JUMP`
<a id="insn-00bcaaec"></a> `00bcaaec` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00bcaaf0"></a> `00bcaaf0` | `3f 01 14 eb` | cmp x9,x20 | `FALL_THROUGH`
<a id="insn-00bcaaf4"></a> `00bcaaf4` | `60 02 00 54` | b.eq 0x00bcab40 | `CONDITIONAL_JUMP`
<a id="insn-00bcaaf8"></a> `00bcaaf8` | `a9 06 40 f9` | ldr x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcaafc"></a> `00bcaafc` | `a9 00 00 b4` | cbz x9,0x00bcab10 | `CONDITIONAL_JUMP`
<a id="insn-00bcab00"></a> `00bcab00` | `f5 03 09 aa` | mov x21,x9 | `FALL_THROUGH`
<a id="insn-00bcab04"></a> `00bcab04` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bcab08"></a> `00bcab08` | `c9 ff ff b5` | cbnz x9,0x00bcab00 | `CONDITIONAL_JUMP`
<a id="insn-00bcab0c"></a> `00bcab0c` | `f6 ff ff 17` | b 0x00bcaae4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcab10"></a> `00bcab10` | `e9 03 15 aa` | mov x9,x21 | `FALL_THROUGH`
<a id="insn-00bcab14"></a> `00bcab14` | `2a 0d 41 f8` | ldr x10,[x9, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcab18"></a> `00bcab18` | `4b 01 40 f9` | ldr x11,[x10] | `FALL_THROUGH`
<a id="insn-00bcab1c"></a> `00bcab1c` | `7f 01 15 eb` | cmp x11,x21 | `FALL_THROUGH`
<a id="insn-00bcab20"></a> `00bcab20` | `00 fe ff 54` | b.eq 0x00bcaae0 | `CONDITIONAL_JUMP`
<a id="insn-00bcab24"></a> `00bcab24` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00bcab28"></a> `00bcab28` | `e9 03 0a aa` | mov x9,x10 | `FALL_THROUGH`
<a id="insn-00bcab2c"></a> `00bcab2c` | `35 0d 41 f8` | ldr x21,[x9, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcab30"></a> `00bcab30` | `ab 02 40 f9` | ldr x11,[x21] | `FALL_THROUGH`
<a id="insn-00bcab34"></a> `00bcab34` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcab38"></a> `00bcab38` | `61 ff ff 54` | b.ne 0x00bcab24 | `CONDITIONAL_JUMP`
<a id="insn-00bcab3c"></a> `00bcab3c` | `ea ff ff 17` | b 0x00bcaae4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcab40"></a> `00bcab40` | `a2 12 40 f9` | ldr x2,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00bcab44"></a> `00bcab44` | `a0 b6 ff b0` | adrp x0,0x29f000 | `FALL_THROUGH`
<a id="insn-00bcab48"></a> `00bcab48` | `00 58 30 91` | add x0,x0,#0xc16 | `FALL_THROUGH`
<a id="insn-00bcab4c"></a> `00bcab4c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcab50"></a> `00bcab50` | `78 41 02 94` | bl 0x00c5b130 | `UNCONDITIONAL_CALL`
<a id="insn-00bcab54"></a> `00bcab54` | `a9 06 40 f9` | ldr x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcab58"></a> `00bcab58` | `a9 00 00 b4` | cbz x9,0x00bcab6c | `CONDITIONAL_JUMP`
<a id="insn-00bcab5c"></a> `00bcab5c` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00bcab60"></a> `00bcab60` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bcab64"></a> `00bcab64` | `c9 ff ff b5` | cbnz x9,0x00bcab5c | `CONDITIONAL_JUMP`
<a id="insn-00bcab68"></a> `00bcab68` | `0c 00 00 14` | b 0x00bcab98 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcab6c"></a> `00bcab6c` | `e9 03 15 aa` | mov x9,x21 | `FALL_THROUGH`
<a id="insn-00bcab70"></a> `00bcab70` | `28 0d 41 f8` | ldr x8,[x9, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcab74"></a> `00bcab74` | `0a 01 40 f9` | ldr x10,[x8] | `FALL_THROUGH`
<a id="insn-00bcab78"></a> `00bcab78` | `5f 01 15 eb` | cmp x10,x21 | `FALL_THROUGH`
<a id="insn-00bcab7c"></a> `00bcab7c` | `e0 00 00 54` | b.eq 0x00bcab98 | `CONDITIONAL_JUMP`
<a id="insn-00bcab80"></a> `00bcab80` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00bcab84"></a> `00bcab84` | `e9 03 0a aa` | mov x9,x10 | `FALL_THROUGH`
<a id="insn-00bcab88"></a> `00bcab88` | `28 0d 41 f8` | ldr x8,[x9, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcab8c"></a> `00bcab8c` | `0b 01 40 f9` | ldr x11,[x8] | `FALL_THROUGH`
<a id="insn-00bcab90"></a> `00bcab90` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcab94"></a> `00bcab94` | `61 ff ff 54` | b.ne 0x00bcab80 | `CONDITIONAL_JUMP`
<a id="insn-00bcab98"></a> `00bcab98` | `c9 02 40 f9` | ldr x9,[x22] | `FALL_THROUGH`
<a id="insn-00bcab9c"></a> `00bcab9c` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bcaba0"></a> `00bcaba0` | `41 00 00 54` | b.ne 0x00bcaba8 | `CONDITIONAL_JUMP`
<a id="insn-00bcaba4"></a> `00bcaba4` | `c8 02 00 f9` | str x8,[x22] | `FALL_THROUGH`
<a id="insn-00bcaba8"></a> `00bcaba8` | `c0 a2 40 a9` | ldp x0,x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bcabac"></a> `00bcabac` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bcabb0"></a> `00bcabb0` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcabb4"></a> `00bcabb4` | `c8 0a 00 f9` | str x8,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00bcabb8"></a> `00bcabb8` | `86 42 02 94` | bl 0x00c5b5d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcabbc"></a> `00bcabbc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcabc0"></a> `00bcabc0` | `bc 34 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcabc4"></a> `00bcabc4` | `95 02 40 f9` | ldr x21,[x20] | `FALL_THROUGH`
<a id="insn-00bcabc8"></a> `00bcabc8` | `d6 0a 40 f9` | ldr x22,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00bcabcc"></a> `00bcabcc` | `a9 1a 41 f9` | ldr x9,[x21, #0x230] | `FALL_THROUGH`
<a id="insn-00bcabd0"></a> `00bcabd0` | `a8 1e 41 f9` | ldr x8,[x21, #0x238] | `FALL_THROUGH`
<a id="insn-00bcabd4"></a> `00bcabd4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcabd8"></a> `00bcabd8` | `80 01 00 54` | b.eq 0x00bcac08 | `CONDITIONAL_JUMP`
<a id="insn-00bcabdc"></a> `00bcabdc` | `a0 06 40 f9` | ldr x0,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcabe0"></a> `00bcabe0` | `01 81 5f f8` | ldur x1,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00bcabe4"></a> `00bcabe4` | `a3 4b 02 94` | bl 0x00c5da70 | `UNCONDITIONAL_CALL`
<a id="insn-00bcabe8"></a> `00bcabe8` | `a9 1a 41 f9` | ldr x9,[x21, #0x230] | `FALL_THROUGH`
<a id="insn-00bcabec"></a> `00bcabec` | `a8 1e 41 f9` | ldr x8,[x21, #0x238] | `FALL_THROUGH`
<a id="insn-00bcabf0"></a> `00bcabf0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcabf4"></a> `00bcabf4` | `41 ff ff 54` | b.ne 0x00bcabdc | `CONDITIONAL_JUMP`
<a id="insn-00bcabf8"></a> `00bcabf8` | `04 00 00 14` | b 0x00bcac08 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcabfc"></a> `00bcabfc` | `a0 06 40 f9` | ldr x0,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcac00"></a> `00bcac00` | `01 81 5f f8` | ldur x1,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00bcac04"></a> `00bcac04` | `97 4b 02 94` | bl 0x00c5da60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcac08"></a> `00bcac08` | `a9 26 41 f9` | ldr x9,[x21, #0x248] | `FALL_THROUGH`
<a id="insn-00bcac0c"></a> `00bcac0c` | `a8 2a 41 f9` | ldr x8,[x21, #0x250] | `FALL_THROUGH`
<a id="insn-00bcac10"></a> `00bcac10` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcac14"></a> `00bcac14` | `41 ff ff 54` | b.ne 0x00bcabfc | `CONDITIONAL_JUMP`
<a id="insn-00bcac18"></a> `00bcac18` | `56 00 00 35` | cbnz w22,0x00bcac20 | `CONDITIONAL_JUMP`
<a id="insn-00bcac1c"></a> `00bcac1c` | `81 4b 02 94` | bl 0x00c5da20 | `UNCONDITIONAL_CALL`
<a id="insn-00bcac20"></a> `00bcac20` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00bcac24"></a> `00bcac24` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcac28"></a> `00bcac28` | `8a 4b 02 94` | bl 0x00c5da50 | `UNCONDITIONAL_CALL`
<a id="insn-00bcac2c"></a> `00bcac2c` | `95 02 40 f9` | ldr x21,[x20] | `FALL_THROUGH`
<a id="insn-00bcac30"></a> `00bcac30` | `b5 00 00 b4` | cbz x21,0x00bcac44 | `CONDITIONAL_JUMP`
<a id="insn-00bcac34"></a> `00bcac34` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcac38"></a> `00bcac38` | `9e 4b 02 94` | bl 0x00c5dab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcac3c"></a> `00bcac3c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcac40"></a> `00bcac40` | `9c 34 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcac44"></a> `00bcac44` | `9f 02 00 f9` | str xzr,[x20] | `FALL_THROUGH`
<a id="insn-00bcac48"></a> `00bcac48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcac4c"></a> `00bcac4c` | `71 3f 02 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcac50"></a> `00bcac50` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcac54"></a> `00bcac54` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcac58"></a> `00bcac58` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcac5c"></a> `00bcac5c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcaa3c`](#insn-00bcaa3c) 範囲 `[['00bcaa3c', '00bcaa6b']]`
  - `CONDITIONAL_JUMP` [`00bcaa68`](#insn-00bcaa68) → [`00bcac48`](#insn-00bcac48)
  - `FALL_THROUGH` [`00bcaa68`](#insn-00bcaa68) → [`00bcaa6c`](#insn-00bcaa6c)
- ブロック [`00bcaa6c`](#insn-00bcaa6c) 範囲 `[['00bcaa6c', '00bcaa8b']]`
  - `FALL_THROUGH` [`00bcaa88`](#insn-00bcaa88) → [`00bcaa8c`](#insn-00bcaa8c)
- ブロック [`00bcaa8c`](#insn-00bcaa8c) 範囲 `[['00bcaa8c', '00bcaa9b']]`
  - `CONDITIONAL_JUMP` [`00bcaa98`](#insn-00bcaa98) → [`00bcaaac`](#insn-00bcaaac)
  - `FALL_THROUGH` [`00bcaa98`](#insn-00bcaa98) → [`00bcaa9c`](#insn-00bcaa9c)
- ブロック [`00bcaa9c`](#insn-00bcaa9c) 範囲 `[['00bcaa9c', '00bcaaab']]`
  - `UNCONDITIONAL_JUMP` [`00bcaaa8`](#insn-00bcaaa8) → [`00bcaa8c`](#insn-00bcaa8c)
- ブロック [`00bcaaac`](#insn-00bcaaac) 範囲 `[['00bcaaac', '00bcaad7']]`
  - `CONDITIONAL_JUMP` [`00bcaad4`](#insn-00bcaad4) → [`00bcabc4`](#insn-00bcabc4)
  - `FALL_THROUGH` [`00bcaad4`](#insn-00bcaad4) → [`00bcaad8`](#insn-00bcaad8)
- ブロック [`00bcaad8`](#insn-00bcaad8) 範囲 `[['00bcaad8', '00bcaadf']]`
  - `UNCONDITIONAL_JUMP` [`00bcaadc`](#insn-00bcaadc) → [`00bcaaec`](#insn-00bcaaec)
- ブロック [`00bcaae0`](#insn-00bcaae0) 範囲 `[['00bcaae0', '00bcaae3']]`
  - `FALL_THROUGH` [`00bcaae0`](#insn-00bcaae0) → [`00bcaae4`](#insn-00bcaae4)
- ブロック [`00bcaae4`](#insn-00bcaae4) 範囲 `[['00bcaae4', '00bcaaeb']]`
  - `CONDITIONAL_JUMP` [`00bcaae8`](#insn-00bcaae8) → [`00bcabc4`](#insn-00bcabc4)
  - `FALL_THROUGH` [`00bcaae8`](#insn-00bcaae8) → [`00bcaaec`](#insn-00bcaaec)
- ブロック [`00bcaaec`](#insn-00bcaaec) 範囲 `[['00bcaaec', '00bcaaf7']]`
  - `CONDITIONAL_JUMP` [`00bcaaf4`](#insn-00bcaaf4) → [`00bcab40`](#insn-00bcab40)
  - `FALL_THROUGH` [`00bcaaf4`](#insn-00bcaaf4) → [`00bcaaf8`](#insn-00bcaaf8)
- ブロック [`00bcaaf8`](#insn-00bcaaf8) 範囲 `[['00bcaaf8', '00bcaaff']]`
  - `CONDITIONAL_JUMP` [`00bcaafc`](#insn-00bcaafc) → [`00bcab10`](#insn-00bcab10)
  - `FALL_THROUGH` [`00bcaafc`](#insn-00bcaafc) → [`00bcab00`](#insn-00bcab00)
- ブロック [`00bcab00`](#insn-00bcab00) 範囲 `[['00bcab00', '00bcab0b']]`
  - `CONDITIONAL_JUMP` [`00bcab08`](#insn-00bcab08) → [`00bcab00`](#insn-00bcab00)
  - `FALL_THROUGH` [`00bcab08`](#insn-00bcab08) → [`00bcab0c`](#insn-00bcab0c)
- ブロック [`00bcab0c`](#insn-00bcab0c) 範囲 `[['00bcab0c', '00bcab0f']]`
  - `UNCONDITIONAL_JUMP` [`00bcab0c`](#insn-00bcab0c) → [`00bcaae4`](#insn-00bcaae4)
- ブロック [`00bcab10`](#insn-00bcab10) 範囲 `[['00bcab10', '00bcab23']]`
  - `CONDITIONAL_JUMP` [`00bcab20`](#insn-00bcab20) → [`00bcaae0`](#insn-00bcaae0)
  - `FALL_THROUGH` [`00bcab20`](#insn-00bcab20) → [`00bcab24`](#insn-00bcab24)
- ブロック [`00bcab24`](#insn-00bcab24) 範囲 `[['00bcab24', '00bcab3b']]`
  - `CONDITIONAL_JUMP` [`00bcab38`](#insn-00bcab38) → [`00bcab24`](#insn-00bcab24)
  - `FALL_THROUGH` [`00bcab38`](#insn-00bcab38) → [`00bcab3c`](#insn-00bcab3c)
- ブロック [`00bcab3c`](#insn-00bcab3c) 範囲 `[['00bcab3c', '00bcab3f']]`
  - `UNCONDITIONAL_JUMP` [`00bcab3c`](#insn-00bcab3c) → [`00bcaae4`](#insn-00bcaae4)
- ブロック [`00bcab40`](#insn-00bcab40) 範囲 `[['00bcab40', '00bcab5b']]`
  - `CONDITIONAL_JUMP` [`00bcab58`](#insn-00bcab58) → [`00bcab6c`](#insn-00bcab6c)
  - `FALL_THROUGH` [`00bcab58`](#insn-00bcab58) → [`00bcab5c`](#insn-00bcab5c)
- ブロック [`00bcab5c`](#insn-00bcab5c) 範囲 `[['00bcab5c', '00bcab67']]`
  - `CONDITIONAL_JUMP` [`00bcab64`](#insn-00bcab64) → [`00bcab5c`](#insn-00bcab5c)
  - `FALL_THROUGH` [`00bcab64`](#insn-00bcab64) → [`00bcab68`](#insn-00bcab68)
- ブロック [`00bcab68`](#insn-00bcab68) 範囲 `[['00bcab68', '00bcab6b']]`
  - `UNCONDITIONAL_JUMP` [`00bcab68`](#insn-00bcab68) → [`00bcab98`](#insn-00bcab98)
- ブロック [`00bcab6c`](#insn-00bcab6c) 範囲 `[['00bcab6c', '00bcab7f']]`
  - `CONDITIONAL_JUMP` [`00bcab7c`](#insn-00bcab7c) → [`00bcab98`](#insn-00bcab98)
  - `FALL_THROUGH` [`00bcab7c`](#insn-00bcab7c) → [`00bcab80`](#insn-00bcab80)
- ブロック [`00bcab80`](#insn-00bcab80) 範囲 `[['00bcab80', '00bcab97']]`
  - `CONDITIONAL_JUMP` [`00bcab94`](#insn-00bcab94) → [`00bcab80`](#insn-00bcab80)
  - `FALL_THROUGH` [`00bcab94`](#insn-00bcab94) → [`00bcab98`](#insn-00bcab98)
- ブロック [`00bcab98`](#insn-00bcab98) 範囲 `[['00bcab98', '00bcaba3']]`
  - `CONDITIONAL_JUMP` [`00bcaba0`](#insn-00bcaba0) → [`00bcaba8`](#insn-00bcaba8)
  - `FALL_THROUGH` [`00bcaba0`](#insn-00bcaba0) → [`00bcaba4`](#insn-00bcaba4)
- ブロック [`00bcaba4`](#insn-00bcaba4) 範囲 `[['00bcaba4', '00bcaba7']]`
  - `FALL_THROUGH` [`00bcaba4`](#insn-00bcaba4) → [`00bcaba8`](#insn-00bcaba8)
- ブロック [`00bcaba8`](#insn-00bcaba8) 範囲 `[['00bcaba8', '00bcabc3']]`
  - `FALL_THROUGH` [`00bcabc0`](#insn-00bcabc0) → [`00bcabc4`](#insn-00bcabc4)
- ブロック [`00bcabc4`](#insn-00bcabc4) 範囲 `[['00bcabc4', '00bcabdb']]`
  - `CONDITIONAL_JUMP` [`00bcabd8`](#insn-00bcabd8) → [`00bcac08`](#insn-00bcac08)
  - `FALL_THROUGH` [`00bcabd8`](#insn-00bcabd8) → [`00bcabdc`](#insn-00bcabdc)
- ブロック [`00bcabdc`](#insn-00bcabdc) 範囲 `[['00bcabdc', '00bcabf7']]`
  - `CONDITIONAL_JUMP` [`00bcabf4`](#insn-00bcabf4) → [`00bcabdc`](#insn-00bcabdc)
  - `FALL_THROUGH` [`00bcabf4`](#insn-00bcabf4) → [`00bcabf8`](#insn-00bcabf8)
- ブロック [`00bcabf8`](#insn-00bcabf8) 範囲 `[['00bcabf8', '00bcabfb']]`
  - `UNCONDITIONAL_JUMP` [`00bcabf8`](#insn-00bcabf8) → [`00bcac08`](#insn-00bcac08)
- ブロック [`00bcabfc`](#insn-00bcabfc) 範囲 `[['00bcabfc', '00bcac07']]`
  - `FALL_THROUGH` [`00bcac04`](#insn-00bcac04) → [`00bcac08`](#insn-00bcac08)
- ブロック [`00bcac08`](#insn-00bcac08) 範囲 `[['00bcac08', '00bcac17']]`
  - `CONDITIONAL_JUMP` [`00bcac14`](#insn-00bcac14) → [`00bcabfc`](#insn-00bcabfc)
  - `FALL_THROUGH` [`00bcac14`](#insn-00bcac14) → [`00bcac18`](#insn-00bcac18)
- ブロック [`00bcac18`](#insn-00bcac18) 範囲 `[['00bcac18', '00bcac1b']]`
  - `CONDITIONAL_JUMP` [`00bcac18`](#insn-00bcac18) → [`00bcac20`](#insn-00bcac20)
  - `FALL_THROUGH` [`00bcac18`](#insn-00bcac18) → [`00bcac1c`](#insn-00bcac1c)
- ブロック [`00bcac1c`](#insn-00bcac1c) 範囲 `[['00bcac1c', '00bcac1f']]`
  - `FALL_THROUGH` [`00bcac1c`](#insn-00bcac1c) → [`00bcac20`](#insn-00bcac20)
- ブロック [`00bcac20`](#insn-00bcac20) 範囲 `[['00bcac20', '00bcac33']]`
  - `CONDITIONAL_JUMP` [`00bcac30`](#insn-00bcac30) → [`00bcac44`](#insn-00bcac44)
  - `FALL_THROUGH` [`00bcac30`](#insn-00bcac30) → [`00bcac34`](#insn-00bcac34)
- ブロック [`00bcac34`](#insn-00bcac34) 範囲 `[['00bcac34', '00bcac43']]`
  - `FALL_THROUGH` [`00bcac40`](#insn-00bcac40) → [`00bcac44`](#insn-00bcac44)
- ブロック [`00bcac44`](#insn-00bcac44) 範囲 `[['00bcac44', '00bcac47']]`
  - `FALL_THROUGH` [`00bcac44`](#insn-00bcac44) → [`00bcac48`](#insn-00bcac48)
- ブロック [`00bcac48`](#insn-00bcac48) 範囲 `[['00bcac48', '00bcac5f']]`

## 命令位置別の参照

- [`00bcaa3c`](#insn-00bcaa3c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa40`](#insn-00bcaa40) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa44`](#insn-00bcaa44) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa50`](#insn-00bcaa50) → `00c9b9a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcaa58`](#insn-00bcaa58) → `01126720`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth13g_auths_mutexE` · 推定型 `undefined8`
- [`00bcaa60`](#insn-00bcaa60) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa68`](#insn-00bcaa68) → [`00bcac48`](#insn-00bcac48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa74`](#insn-00bcaa74) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa88`](#insn-00bcaa88) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa94`](#insn-00bcaa94) → [`00c5bce0`](../00c5b/00c5bce0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bce0` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa98`](#insn-00bcaa98) → [`00bcaaac`](#insn-00bcaaac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaaa4`](#insn-00bcaaa4) → [`00c5db20`](../00c5d/00c5db20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5db20` · 推定シンボル `None` · 推定型 `None`
- [`00bcaaa8`](#insn-00bcaaa8) → [`00bcaa8c`](#insn-00bcaa8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaab4`](#insn-00bcaab4) → [`00c5abf0`](../00c5a/00c5abf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5abf0` · 推定シンボル `None` · 推定型 `None`
- [`00bcaabc`](#insn-00bcaabc) → [`00c5ac10`](../00c5a/00c5ac10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac10` · 推定シンボル `None` · 推定型 `None`
- [`00bcaac4`](#insn-00bcaac4) → `00c9b9a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcaacc`](#insn-00bcaacc) → `01126708`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth7g_authsE` · 推定型 `undefined8`
- [`00bcaad4`](#insn-00bcaad4) → [`00bcabc4`](#insn-00bcabc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaadc`](#insn-00bcaadc) → [`00bcaaec`](#insn-00bcaaec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaae8`](#insn-00bcaae8) → [`00bcabc4`](#insn-00bcabc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaaf4`](#insn-00bcaaf4) → [`00bcab40`](#insn-00bcab40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaafc`](#insn-00bcaafc) → [`00bcab10`](#insn-00bcab10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab08`](#insn-00bcab08) → [`00bcab00`](#insn-00bcab00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab0c`](#insn-00bcab0c) → [`00bcaae4`](#insn-00bcaae4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab20`](#insn-00bcab20) → [`00bcaae0`](#insn-00bcaae0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab38`](#insn-00bcab38) → [`00bcab24`](#insn-00bcab24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab3c`](#insn-00bcab3c) → [`00bcaae4`](#insn-00bcaae4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab48`](#insn-00bcab48) → `0029fc16`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcab50`](#insn-00bcab50) → [`00c5b130`](../00c5b/00c5b130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b130` · 推定シンボル `None` · 推定型 `None`
- [`00bcab58`](#insn-00bcab58) → [`00bcab6c`](#insn-00bcab6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab64`](#insn-00bcab64) → [`00bcab5c`](#insn-00bcab5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab68`](#insn-00bcab68) → [`00bcab98`](#insn-00bcab98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab7c`](#insn-00bcab7c) → [`00bcab98`](#insn-00bcab98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab94`](#insn-00bcab94) → [`00bcab80`](#insn-00bcab80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab98`](#insn-00bcab98) → `01126708`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth7g_authsE` · 推定型 `undefined8`
- [`00bcaba0`](#insn-00bcaba0) → [`00bcaba8`](#insn-00bcaba8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaba4`](#insn-00bcaba4) → `01126708`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth7g_authsE` · 推定型 `undefined8`
- [`00bcaba8`](#insn-00bcaba8) → `01126710`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcaba8`](#insn-00bcaba8) → `01126718`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcabb4`](#insn-00bcabb4) → `01126718`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcabb8`](#insn-00bcabb8) → [`00c5b5d0`](../00c5b/00c5b5d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b5d0` · 推定シンボル `None` · 推定型 `None`
- [`00bcabc0`](#insn-00bcabc0) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcabc8`](#insn-00bcabc8) → `01126718`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcabd8`](#insn-00bcabd8) → [`00bcac08`](#insn-00bcac08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcabe4`](#insn-00bcabe4) → [`00c5da70`](../00c5d/00c5da70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5da70` · 推定シンボル `None` · 推定型 `None`
- [`00bcabf4`](#insn-00bcabf4) → [`00bcabdc`](#insn-00bcabdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcabf8`](#insn-00bcabf8) → [`00bcac08`](#insn-00bcac08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac04`](#insn-00bcac04) → [`00c5da60`](../00c5d/00c5da60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5da60` · 推定シンボル `None` · 推定型 `None`
- [`00bcac14`](#insn-00bcac14) → [`00bcabfc`](#insn-00bcabfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac18`](#insn-00bcac18) → [`00bcac20`](#insn-00bcac20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac1c`](#insn-00bcac1c) → [`00c5da20`](../00c5d/00c5da20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5da20` · 推定シンボル `None` · 推定型 `None`
- [`00bcac28`](#insn-00bcac28) → [`00c5da50`](../00c5d/00c5da50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5da50` · 推定シンボル `None` · 推定型 `None`
- [`00bcac30`](#insn-00bcac30) → [`00bcac44`](#insn-00bcac44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac38`](#insn-00bcac38) → [`00c5dab0`](../00c5d/00c5dab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dab0` · 推定シンボル `None` · 推定型 `None`
- [`00bcac40`](#insn-00bcac40) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcac4c`](#insn-00bcac4c) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00bcac50`](#insn-00bcac50) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac54`](#insn-00bcac54) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcaa3c`](#insn-00bcaa3c)

~~~json
{
  "source": "00bcaa3c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaa40`](#insn-00bcaa40)

~~~json
{
  "source": "00bcaa40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaa44`](#insn-00bcaa44)

~~~json
{
  "source": "00bcaa44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaa50`](#insn-00bcaa50)

~~~json
{
  "source": "00bcaa50",
  "target": "00c9b9a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b9a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcaa58`](#insn-00bcaa58)

~~~json
{
  "source": "00bcaa58",
  "target": "01126720",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126720",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcaa60`](#insn-00bcaa60)

~~~json
{
  "source": "00bcaa60",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcaa68`](#insn-00bcaa68)

~~~json
{
  "source": "00bcaa68",
  "target": "00bcac48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaa74`](#insn-00bcaa74)

~~~json
{
  "source": "00bcaa74",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcaa88`](#insn-00bcaa88)

~~~json
{
  "source": "00bcaa88",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcaa94`](#insn-00bcaa94)

~~~json
{
  "source": "00bcaa94",
  "target": "00c5bce0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcaa98`](#insn-00bcaa98)

~~~json
{
  "source": "00bcaa98",
  "target": "00bcaaac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaaa4`](#insn-00bcaaa4)

~~~json
{
  "source": "00bcaaa4",
  "target": "00c5db20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcaaa8`](#insn-00bcaaa8)

~~~json
{
  "source": "00bcaaa8",
  "target": "00bcaa8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaab4`](#insn-00bcaab4)

~~~json
{
  "source": "00bcaab4",
  "target": "00c5abf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcaabc`](#insn-00bcaabc)

~~~json
{
  "source": "00bcaabc",
  "target": "00c5ac10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcaac4`](#insn-00bcaac4)

~~~json
{
  "source": "00bcaac4",
  "target": "00c9b9a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b9a8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcaacc`](#insn-00bcaacc)

~~~json
{
  "source": "00bcaacc",
  "target": "01126708",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126708",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcaad4`](#insn-00bcaad4)

~~~json
{
  "source": "00bcaad4",
  "target": "00bcabc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaadc`](#insn-00bcaadc)

~~~json
{
  "source": "00bcaadc",
  "target": "00bcaaec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaae8`](#insn-00bcaae8)

~~~json
{
  "source": "00bcaae8",
  "target": "00bcabc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaaf4`](#insn-00bcaaf4)

~~~json
{
  "source": "00bcaaf4",
  "target": "00bcab40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaafc`](#insn-00bcaafc)

~~~json
{
  "source": "00bcaafc",
  "target": "00bcab10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab08`](#insn-00bcab08)

~~~json
{
  "source": "00bcab08",
  "target": "00bcab00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab0c`](#insn-00bcab0c)

~~~json
{
  "source": "00bcab0c",
  "target": "00bcaae4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab20`](#insn-00bcab20)

~~~json
{
  "source": "00bcab20",
  "target": "00bcaae0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab38`](#insn-00bcab38)

~~~json
{
  "source": "00bcab38",
  "target": "00bcab24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab3c`](#insn-00bcab3c)

~~~json
{
  "source": "00bcab3c",
  "target": "00bcaae4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab48`](#insn-00bcab48)

~~~json
{
  "source": "00bcab48",
  "target": "0029fc16",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029fc16",
  "offset": 0,
  "size": 28,
  "datatype": "string",
  "bytes": "44656c6574696e67204175746820257020666f722041707020257000",
  "capture_start": "0029fc16",
  "capture_bytes": 28,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcab50`](#insn-00bcab50)

~~~json
{
  "source": "00bcab50",
  "target": "00c5b130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcab58`](#insn-00bcab58)

~~~json
{
  "source": "00bcab58",
  "target": "00bcab6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab64`](#insn-00bcab64)

~~~json
{
  "source": "00bcab64",
  "target": "00bcab5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab68`](#insn-00bcab68)

~~~json
{
  "source": "00bcab68",
  "target": "00bcab98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab7c`](#insn-00bcab7c)

~~~json
{
  "source": "00bcab7c",
  "target": "00bcab98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab94`](#insn-00bcab94)

~~~json
{
  "source": "00bcab94",
  "target": "00bcab80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab98`](#insn-00bcab98)

~~~json
{
  "source": "00bcab98",
  "target": "01126708",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126708",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcaba0`](#insn-00bcaba0)

~~~json
{
  "source": "00bcaba0",
  "target": "00bcaba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaba4`](#insn-00bcaba4)

~~~json
{
  "source": "00bcaba4",
  "target": "01126708",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126708",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcaba8`](#insn-00bcaba8)

~~~json
{
  "source": "00bcaba8",
  "target": "01126710",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126710",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcaba8`](#insn-00bcaba8)

~~~json
{
  "source": "00bcaba8",
  "target": "01126718",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126718",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcabb4`](#insn-00bcabb4)

~~~json
{
  "source": "00bcabb4",
  "target": "01126718",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126718",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcabb8`](#insn-00bcabb8)

~~~json
{
  "source": "00bcabb8",
  "target": "00c5b5d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcabc0`](#insn-00bcabc0)

~~~json
{
  "source": "00bcabc0",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcabc8`](#insn-00bcabc8)

~~~json
{
  "source": "00bcabc8",
  "target": "01126718",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126718",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcabd8`](#insn-00bcabd8)

~~~json
{
  "source": "00bcabd8",
  "target": "00bcac08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcabe4`](#insn-00bcabe4)

~~~json
{
  "source": "00bcabe4",
  "target": "00c5da70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcabf4`](#insn-00bcabf4)

~~~json
{
  "source": "00bcabf4",
  "target": "00bcabdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcabf8`](#insn-00bcabf8)

~~~json
{
  "source": "00bcabf8",
  "target": "00bcac08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac04`](#insn-00bcac04)

~~~json
{
  "source": "00bcac04",
  "target": "00c5da60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcac14`](#insn-00bcac14)

~~~json
{
  "source": "00bcac14",
  "target": "00bcabfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac18`](#insn-00bcac18)

~~~json
{
  "source": "00bcac18",
  "target": "00bcac20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac1c`](#insn-00bcac1c)

~~~json
{
  "source": "00bcac1c",
  "target": "00c5da20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcac28`](#insn-00bcac28)

~~~json
{
  "source": "00bcac28",
  "target": "00c5da50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcac30`](#insn-00bcac30)

~~~json
{
  "source": "00bcac30",
  "target": "00bcac44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac38`](#insn-00bcac38)

~~~json
{
  "source": "00bcac38",
  "target": "00c5dab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcac40`](#insn-00bcac40)

~~~json
{
  "source": "00bcac40",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcac4c`](#insn-00bcac4c)

~~~json
{
  "source": "00bcac4c",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcac50`](#insn-00bcac50)

~~~json
{
  "source": "00bcac50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac54`](#insn-00bcac54)

~~~json
{
  "source": "00bcac54",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
