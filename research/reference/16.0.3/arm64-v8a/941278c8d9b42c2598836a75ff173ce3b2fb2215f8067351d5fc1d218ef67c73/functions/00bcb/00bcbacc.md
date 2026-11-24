# 00bcbacc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcaad8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcaad8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-33cb128aa830b48b07e84eb5613d2130)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbacc",
  "name": "_ZN8firebase4auth4Auth14DeleteInternalEv",
  "size": 548,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a424fa94cb63d18b51e0244c285c28be769d6a7dd3c83cf3f73352e9f29da45f",
  "source_text_sha256": "a424fa94cb63d18b51e0244c285c28be769d6a7dd3c83cf3f73352e9f29da45f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbacc",
        "00bcbcef"
      ]
    ],
    "bytes_sha256": "23a27bd94526ca44bad14a339ce2cb28de9108bd72744250fc4b8af8195ade4d",
    "instruction_count": 137,
    "instruction_bytes": 548,
    "body_bytes": 548,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5ead0](../00c5e/00c5ead0.md)

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)
- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5bc90](../00c5b/00c5bc90.md)
- [00c5bcb0](../00c5b/00c5bcb0.md)
- [00c5c1d0](../00c5c/00c5c1d0.md)
- [00c5c670](../00c5c/00c5c670.md)
- [00c5cd80](../00c5c/00c5cd80.md)
- [00c5eac0](../00c5e/00c5eac0.md)
- [00c5eaf0](../00c5e/00c5eaf0.md)
- [00c5eb00](../00c5e/00c5eb00.md)
- [00c5eb10](../00c5e/00c5eb10.md)
- [00c5eb50](../00c5e/00c5eb50.md)
- [00c5ebc0](../00c5e/00c5ebc0.md)

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
  
  uVar7 = *(undefined8 *)PTR__ZN8firebase4auth13g_auths_mutexE_00c9ca40;
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
    puVar1 = PTR__ZN8firebase4auth7g_authsE_00c9ca48;
    if (*(long **)PTR__ZN8firebase4auth7g_authsE_00c9ca48 !=
        (long *)(PTR__ZN8firebase4auth7g_authsE_00c9ca48 + 8)) {
      __ptr = *(long **)PTR__ZN8firebase4auth7g_authsE_00c9ca48;
LAB_00bcbb7c:
      if ((long *)__ptr[5] != param_1) goto code_r0x00bcbb88;
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
LAB_00bcbc54:
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
code_r0x00bcbb88:
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
  if (plVar6 == (long *)(PTR__ZN8firebase4auth7g_authsE_00c9ca48 + 8)) goto LAB_00bcbc54;
  goto LAB_00bcbb7c;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbacc"></a> `00bcbacc` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcbad0"></a> `00bcbad0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbad4"></a> `00bcbad4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbad8"></a> `00bcbad8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcbadc"></a> `00bcbadc` | `88 06 00 b0` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bcbae0"></a> `00bcbae0` | `08 21 45 f9` | ldr x8,[x8, #0xa40] | `FALL_THROUGH`
<a id="insn-00bcbae4"></a> `00bcbae4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcbae8"></a> `00bcbae8` | `13 01 40 f9` | ldr x19,[x8] | `FALL_THROUGH`
<a id="insn-00bcbaec"></a> `00bcbaec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcbaf0"></a> `00bcbaf0` | `ec 3f 02 94` | bl 0x00c5baa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbaf4"></a> `00bcbaf4` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcbaf8"></a> `00bcbaf8` | `08 0f 00 b4` | cbz x8,0x00bcbcd8 | `CONDITIONAL_JUMP`
<a id="insn-00bcbafc"></a> `00bcbafc` | `15 a1 0b 91` | add x21,x8,#0x2e8 | `FALL_THROUGH`
<a id="insn-00bcbb00"></a> `00bcbb00` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcbb04"></a> `00bcbb04` | `e7 3f 02 94` | bl 0x00c5baa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbb08"></a> `00bcbb08` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcbb0c"></a> `00bcbb0c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbb10"></a> `00bcbb10` | `09 91 0b 39` | strb w9,[x8, #0x2e4] | `FALL_THROUGH`
<a id="insn-00bcbb14"></a> `00bcbb14` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcbb18"></a> `00bcbb18` | `e6 3f 02 94` | bl 0x00c5bab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbb1c"></a> `00bcbb1c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcbb20"></a> `00bcbb20` | `00 41 00 91` | add x0,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bcbb24"></a> `00bcbb24` | `97 44 02 94` | bl 0x00c5cd80 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbb28"></a> `00bcbb28` | `a0 00 00 37` | tbnz w0,#0x0,0x00bcbb3c | `CONDITIONAL_JUMP`
<a id="insn-00bcbb2c"></a> `00bcbb2c` | `00 d4 90 52` | mov w0,#0x86a0 | `FALL_THROUGH`
<a id="insn-00bcbb30"></a> `00bcbb30` | `20 00 a0 72` | movk w0,#0x1, LSL #16 | `FALL_THROUGH`
<a id="insn-00bcbb34"></a> `00bcbb34` | `23 4c 02 94` | bl 0x00c5ebc0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbb38"></a> `00bcbb38` | `f9 ff ff 17` | b 0x00bcbb1c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcbb3c"></a> `00bcbb3c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcbb40"></a> `00bcbb40` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bcbb44"></a> `00bcbb44` | `53 40 02 94` | bl 0x00c5bc90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbb48"></a> `00bcbb48` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcbb4c"></a> `00bcbb4c` | `59 40 02 94` | bl 0x00c5bcb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbb50"></a> `00bcbb50` | `96 06 00 b0` | adrp x22,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bcbb54"></a> `00bcbb54` | `d6 26 45 f9` | ldr x22,[x22, #0xa48] | `FALL_THROUGH`
<a id="insn-00bcbb58"></a> `00bcbb58` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bcbb5c"></a> `00bcbb5c` | `15 85 40 f8` | ldr x21,[x8], #0x8 | `FALL_THROUGH`
<a id="insn-00bcbb60"></a> `00bcbb60` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00bcbb64"></a> `00bcbb64` | `80 07 00 54` | b.eq 0x00bcbc54 | `CONDITIONAL_JUMP`
<a id="insn-00bcbb68"></a> `00bcbb68` | `c8 22 00 91` | add x8,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00bcbb6c"></a> `00bcbb6c` | `04 00 00 14` | b 0x00bcbb7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcbb70"></a> `00bcbb70` | `f5 03 0a aa` | mov x21,x10 | `FALL_THROUGH`
<a id="insn-00bcbb74"></a> `00bcbb74` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00bcbb78"></a> `00bcbb78` | `e0 06 00 54` | b.eq 0x00bcbc54 | `CONDITIONAL_JUMP`
<a id="insn-00bcbb7c"></a> `00bcbb7c` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00bcbb80"></a> `00bcbb80` | `3f 01 14 eb` | cmp x9,x20 | `FALL_THROUGH`
<a id="insn-00bcbb84"></a> `00bcbb84` | `60 02 00 54` | b.eq 0x00bcbbd0 | `CONDITIONAL_JUMP`
<a id="insn-00bcbb88"></a> `00bcbb88` | `a9 06 40 f9` | ldr x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbb8c"></a> `00bcbb8c` | `a9 00 00 b4` | cbz x9,0x00bcbba0 | `CONDITIONAL_JUMP`
<a id="insn-00bcbb90"></a> `00bcbb90` | `f5 03 09 aa` | mov x21,x9 | `FALL_THROUGH`
<a id="insn-00bcbb94"></a> `00bcbb94` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bcbb98"></a> `00bcbb98` | `c9 ff ff b5` | cbnz x9,0x00bcbb90 | `CONDITIONAL_JUMP`
<a id="insn-00bcbb9c"></a> `00bcbb9c` | `f6 ff ff 17` | b 0x00bcbb74 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcbba0"></a> `00bcbba0` | `e9 03 15 aa` | mov x9,x21 | `FALL_THROUGH`
<a id="insn-00bcbba4"></a> `00bcbba4` | `2a 0d 41 f8` | ldr x10,[x9, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcbba8"></a> `00bcbba8` | `4b 01 40 f9` | ldr x11,[x10] | `FALL_THROUGH`
<a id="insn-00bcbbac"></a> `00bcbbac` | `7f 01 15 eb` | cmp x11,x21 | `FALL_THROUGH`
<a id="insn-00bcbbb0"></a> `00bcbbb0` | `00 fe ff 54` | b.eq 0x00bcbb70 | `CONDITIONAL_JUMP`
<a id="insn-00bcbbb4"></a> `00bcbbb4` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00bcbbb8"></a> `00bcbbb8` | `e9 03 0a aa` | mov x9,x10 | `FALL_THROUGH`
<a id="insn-00bcbbbc"></a> `00bcbbbc` | `35 0d 41 f8` | ldr x21,[x9, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcbbc0"></a> `00bcbbc0` | `ab 02 40 f9` | ldr x11,[x21] | `FALL_THROUGH`
<a id="insn-00bcbbc4"></a> `00bcbbc4` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcbbc8"></a> `00bcbbc8` | `61 ff ff 54` | b.ne 0x00bcbbb4 | `CONDITIONAL_JUMP`
<a id="insn-00bcbbcc"></a> `00bcbbcc` | `ea ff ff 17` | b 0x00bcbb74 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcbbd0"></a> `00bcbbd0` | `a2 12 40 f9` | ldr x2,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbbd4"></a> `00bcbbd4` | `a0 b6 ff 90` | adrp x0,0x29f000 | `FALL_THROUGH`
<a id="insn-00bcbbd8"></a> `00bcbbd8` | `00 24 30 91` | add x0,x0,#0xc09 | `FALL_THROUGH`
<a id="insn-00bcbbdc"></a> `00bcbbdc` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcbbe0"></a> `00bcbbe0` | `7c 41 02 94` | bl 0x00c5c1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbbe4"></a> `00bcbbe4` | `a9 06 40 f9` | ldr x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbbe8"></a> `00bcbbe8` | `a9 00 00 b4` | cbz x9,0x00bcbbfc | `CONDITIONAL_JUMP`
<a id="insn-00bcbbec"></a> `00bcbbec` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00bcbbf0"></a> `00bcbbf0` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bcbbf4"></a> `00bcbbf4` | `c9 ff ff b5` | cbnz x9,0x00bcbbec | `CONDITIONAL_JUMP`
<a id="insn-00bcbbf8"></a> `00bcbbf8` | `0c 00 00 14` | b 0x00bcbc28 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcbbfc"></a> `00bcbbfc` | `e9 03 15 aa` | mov x9,x21 | `FALL_THROUGH`
<a id="insn-00bcbc00"></a> `00bcbc00` | `28 0d 41 f8` | ldr x8,[x9, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcbc04"></a> `00bcbc04` | `0a 01 40 f9` | ldr x10,[x8] | `FALL_THROUGH`
<a id="insn-00bcbc08"></a> `00bcbc08` | `5f 01 15 eb` | cmp x10,x21 | `FALL_THROUGH`
<a id="insn-00bcbc0c"></a> `00bcbc0c` | `e0 00 00 54` | b.eq 0x00bcbc28 | `CONDITIONAL_JUMP`
<a id="insn-00bcbc10"></a> `00bcbc10` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00bcbc14"></a> `00bcbc14` | `e9 03 0a aa` | mov x9,x10 | `FALL_THROUGH`
<a id="insn-00bcbc18"></a> `00bcbc18` | `28 0d 41 f8` | ldr x8,[x9, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcbc1c"></a> `00bcbc1c` | `0b 01 40 f9` | ldr x11,[x8] | `FALL_THROUGH`
<a id="insn-00bcbc20"></a> `00bcbc20` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcbc24"></a> `00bcbc24` | `61 ff ff 54` | b.ne 0x00bcbc10 | `CONDITIONAL_JUMP`
<a id="insn-00bcbc28"></a> `00bcbc28` | `c9 02 40 f9` | ldr x9,[x22] | `FALL_THROUGH`
<a id="insn-00bcbc2c"></a> `00bcbc2c` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bcbc30"></a> `00bcbc30` | `41 00 00 54` | b.ne 0x00bcbc38 | `CONDITIONAL_JUMP`
<a id="insn-00bcbc34"></a> `00bcbc34` | `c8 02 00 f9` | str x8,[x22] | `FALL_THROUGH`
<a id="insn-00bcbc38"></a> `00bcbc38` | `c0 a2 40 a9` | ldp x0,x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbc3c"></a> `00bcbc3c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bcbc40"></a> `00bcbc40` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbc44"></a> `00bcbc44` | `c8 0a 00 f9` | str x8,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbc48"></a> `00bcbc48` | `8a 42 02 94` | bl 0x00c5c670 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbc4c"></a> `00bcbc4c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcbc50"></a> `00bcbc50` | `c0 34 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbc54"></a> `00bcbc54` | `95 02 40 f9` | ldr x21,[x20] | `FALL_THROUGH`
<a id="insn-00bcbc58"></a> `00bcbc58` | `d6 0a 40 f9` | ldr x22,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbc5c"></a> `00bcbc5c` | `a9 1a 41 f9` | ldr x9,[x21, #0x230] | `FALL_THROUGH`
<a id="insn-00bcbc60"></a> `00bcbc60` | `a8 1e 41 f9` | ldr x8,[x21, #0x238] | `FALL_THROUGH`
<a id="insn-00bcbc64"></a> `00bcbc64` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcbc68"></a> `00bcbc68` | `80 01 00 54` | b.eq 0x00bcbc98 | `CONDITIONAL_JUMP`
<a id="insn-00bcbc6c"></a> `00bcbc6c` | `a0 06 40 f9` | ldr x0,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbc70"></a> `00bcbc70` | `01 81 5f f8` | ldur x1,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00bcbc74"></a> `00bcbc74` | `a7 4b 02 94` | bl 0x00c5eb10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbc78"></a> `00bcbc78` | `a9 1a 41 f9` | ldr x9,[x21, #0x230] | `FALL_THROUGH`
<a id="insn-00bcbc7c"></a> `00bcbc7c` | `a8 1e 41 f9` | ldr x8,[x21, #0x238] | `FALL_THROUGH`
<a id="insn-00bcbc80"></a> `00bcbc80` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcbc84"></a> `00bcbc84` | `41 ff ff 54` | b.ne 0x00bcbc6c | `CONDITIONAL_JUMP`
<a id="insn-00bcbc88"></a> `00bcbc88` | `04 00 00 14` | b 0x00bcbc98 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcbc8c"></a> `00bcbc8c` | `a0 06 40 f9` | ldr x0,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbc90"></a> `00bcbc90` | `01 81 5f f8` | ldur x1,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00bcbc94"></a> `00bcbc94` | `9b 4b 02 94` | bl 0x00c5eb00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbc98"></a> `00bcbc98` | `a9 26 41 f9` | ldr x9,[x21, #0x248] | `FALL_THROUGH`
<a id="insn-00bcbc9c"></a> `00bcbc9c` | `a8 2a 41 f9` | ldr x8,[x21, #0x250] | `FALL_THROUGH`
<a id="insn-00bcbca0"></a> `00bcbca0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcbca4"></a> `00bcbca4` | `41 ff ff 54` | b.ne 0x00bcbc8c | `CONDITIONAL_JUMP`
<a id="insn-00bcbca8"></a> `00bcbca8` | `56 00 00 35` | cbnz w22,0x00bcbcb0 | `CONDITIONAL_JUMP`
<a id="insn-00bcbcac"></a> `00bcbcac` | `85 4b 02 94` | bl 0x00c5eac0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbcb0"></a> `00bcbcb0` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00bcbcb4"></a> `00bcbcb4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbcb8"></a> `00bcbcb8` | `8e 4b 02 94` | bl 0x00c5eaf0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbcbc"></a> `00bcbcbc` | `95 02 40 f9` | ldr x21,[x20] | `FALL_THROUGH`
<a id="insn-00bcbcc0"></a> `00bcbcc0` | `b5 00 00 b4` | cbz x21,0x00bcbcd4 | `CONDITIONAL_JUMP`
<a id="insn-00bcbcc4"></a> `00bcbcc4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcbcc8"></a> `00bcbcc8` | `a2 4b 02 94` | bl 0x00c5eb50 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbccc"></a> `00bcbccc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcbcd0"></a> `00bcbcd0` | `a0 34 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbcd4"></a> `00bcbcd4` | `9f 02 00 f9` | str xzr,[x20] | `FALL_THROUGH`
<a id="insn-00bcbcd8"></a> `00bcbcd8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcbcdc"></a> `00bcbcdc` | `75 3f 02 94` | bl 0x00c5bab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbce0"></a> `00bcbce0` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbce4"></a> `00bcbce4` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbce8"></a> `00bcbce8` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcbcec"></a> `00bcbcec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbacc`](#insn-00bcbacc) 範囲 `[['00bcbacc', '00bcbafb']]`
  - `CONDITIONAL_JUMP` [`00bcbaf8`](#insn-00bcbaf8) → [`00bcbcd8`](#insn-00bcbcd8)
  - `FALL_THROUGH` [`00bcbaf8`](#insn-00bcbaf8) → [`00bcbafc`](#insn-00bcbafc)
- ブロック [`00bcbafc`](#insn-00bcbafc) 範囲 `[['00bcbafc', '00bcbb1b']]`
  - `FALL_THROUGH` [`00bcbb18`](#insn-00bcbb18) → [`00bcbb1c`](#insn-00bcbb1c)
- ブロック [`00bcbb1c`](#insn-00bcbb1c) 範囲 `[['00bcbb1c', '00bcbb2b']]`
  - `CONDITIONAL_JUMP` [`00bcbb28`](#insn-00bcbb28) → [`00bcbb3c`](#insn-00bcbb3c)
  - `FALL_THROUGH` [`00bcbb28`](#insn-00bcbb28) → [`00bcbb2c`](#insn-00bcbb2c)
- ブロック [`00bcbb2c`](#insn-00bcbb2c) 範囲 `[['00bcbb2c', '00bcbb3b']]`
  - `UNCONDITIONAL_JUMP` [`00bcbb38`](#insn-00bcbb38) → [`00bcbb1c`](#insn-00bcbb1c)
- ブロック [`00bcbb3c`](#insn-00bcbb3c) 範囲 `[['00bcbb3c', '00bcbb67']]`
  - `CONDITIONAL_JUMP` [`00bcbb64`](#insn-00bcbb64) → [`00bcbc54`](#insn-00bcbc54)
  - `FALL_THROUGH` [`00bcbb64`](#insn-00bcbb64) → [`00bcbb68`](#insn-00bcbb68)
- ブロック [`00bcbb68`](#insn-00bcbb68) 範囲 `[['00bcbb68', '00bcbb6f']]`
  - `UNCONDITIONAL_JUMP` [`00bcbb6c`](#insn-00bcbb6c) → [`00bcbb7c`](#insn-00bcbb7c)
- ブロック [`00bcbb70`](#insn-00bcbb70) 範囲 `[['00bcbb70', '00bcbb73']]`
  - `FALL_THROUGH` [`00bcbb70`](#insn-00bcbb70) → [`00bcbb74`](#insn-00bcbb74)
- ブロック [`00bcbb74`](#insn-00bcbb74) 範囲 `[['00bcbb74', '00bcbb7b']]`
  - `CONDITIONAL_JUMP` [`00bcbb78`](#insn-00bcbb78) → [`00bcbc54`](#insn-00bcbc54)
  - `FALL_THROUGH` [`00bcbb78`](#insn-00bcbb78) → [`00bcbb7c`](#insn-00bcbb7c)
- ブロック [`00bcbb7c`](#insn-00bcbb7c) 範囲 `[['00bcbb7c', '00bcbb87']]`
  - `CONDITIONAL_JUMP` [`00bcbb84`](#insn-00bcbb84) → [`00bcbbd0`](#insn-00bcbbd0)
  - `FALL_THROUGH` [`00bcbb84`](#insn-00bcbb84) → [`00bcbb88`](#insn-00bcbb88)
- ブロック [`00bcbb88`](#insn-00bcbb88) 範囲 `[['00bcbb88', '00bcbb8f']]`
  - `CONDITIONAL_JUMP` [`00bcbb8c`](#insn-00bcbb8c) → [`00bcbba0`](#insn-00bcbba0)
  - `FALL_THROUGH` [`00bcbb8c`](#insn-00bcbb8c) → [`00bcbb90`](#insn-00bcbb90)
- ブロック [`00bcbb90`](#insn-00bcbb90) 範囲 `[['00bcbb90', '00bcbb9b']]`
  - `CONDITIONAL_JUMP` [`00bcbb98`](#insn-00bcbb98) → [`00bcbb90`](#insn-00bcbb90)
  - `FALL_THROUGH` [`00bcbb98`](#insn-00bcbb98) → [`00bcbb9c`](#insn-00bcbb9c)
- ブロック [`00bcbb9c`](#insn-00bcbb9c) 範囲 `[['00bcbb9c', '00bcbb9f']]`
  - `UNCONDITIONAL_JUMP` [`00bcbb9c`](#insn-00bcbb9c) → [`00bcbb74`](#insn-00bcbb74)
- ブロック [`00bcbba0`](#insn-00bcbba0) 範囲 `[['00bcbba0', '00bcbbb3']]`
  - `CONDITIONAL_JUMP` [`00bcbbb0`](#insn-00bcbbb0) → [`00bcbb70`](#insn-00bcbb70)
  - `FALL_THROUGH` [`00bcbbb0`](#insn-00bcbbb0) → [`00bcbbb4`](#insn-00bcbbb4)
- ブロック [`00bcbbb4`](#insn-00bcbbb4) 範囲 `[['00bcbbb4', '00bcbbcb']]`
  - `CONDITIONAL_JUMP` [`00bcbbc8`](#insn-00bcbbc8) → [`00bcbbb4`](#insn-00bcbbb4)
  - `FALL_THROUGH` [`00bcbbc8`](#insn-00bcbbc8) → [`00bcbbcc`](#insn-00bcbbcc)
- ブロック [`00bcbbcc`](#insn-00bcbbcc) 範囲 `[['00bcbbcc', '00bcbbcf']]`
  - `UNCONDITIONAL_JUMP` [`00bcbbcc`](#insn-00bcbbcc) → [`00bcbb74`](#insn-00bcbb74)
- ブロック [`00bcbbd0`](#insn-00bcbbd0) 範囲 `[['00bcbbd0', '00bcbbeb']]`
  - `CONDITIONAL_JUMP` [`00bcbbe8`](#insn-00bcbbe8) → [`00bcbbfc`](#insn-00bcbbfc)
  - `FALL_THROUGH` [`00bcbbe8`](#insn-00bcbbe8) → [`00bcbbec`](#insn-00bcbbec)
- ブロック [`00bcbbec`](#insn-00bcbbec) 範囲 `[['00bcbbec', '00bcbbf7']]`
  - `CONDITIONAL_JUMP` [`00bcbbf4`](#insn-00bcbbf4) → [`00bcbbec`](#insn-00bcbbec)
  - `FALL_THROUGH` [`00bcbbf4`](#insn-00bcbbf4) → [`00bcbbf8`](#insn-00bcbbf8)
- ブロック [`00bcbbf8`](#insn-00bcbbf8) 範囲 `[['00bcbbf8', '00bcbbfb']]`
  - `UNCONDITIONAL_JUMP` [`00bcbbf8`](#insn-00bcbbf8) → [`00bcbc28`](#insn-00bcbc28)
- ブロック [`00bcbbfc`](#insn-00bcbbfc) 範囲 `[['00bcbbfc', '00bcbc0f']]`
  - `CONDITIONAL_JUMP` [`00bcbc0c`](#insn-00bcbc0c) → [`00bcbc28`](#insn-00bcbc28)
  - `FALL_THROUGH` [`00bcbc0c`](#insn-00bcbc0c) → [`00bcbc10`](#insn-00bcbc10)
- ブロック [`00bcbc10`](#insn-00bcbc10) 範囲 `[['00bcbc10', '00bcbc27']]`
  - `CONDITIONAL_JUMP` [`00bcbc24`](#insn-00bcbc24) → [`00bcbc10`](#insn-00bcbc10)
  - `FALL_THROUGH` [`00bcbc24`](#insn-00bcbc24) → [`00bcbc28`](#insn-00bcbc28)
- ブロック [`00bcbc28`](#insn-00bcbc28) 範囲 `[['00bcbc28', '00bcbc33']]`
  - `CONDITIONAL_JUMP` [`00bcbc30`](#insn-00bcbc30) → [`00bcbc38`](#insn-00bcbc38)
  - `FALL_THROUGH` [`00bcbc30`](#insn-00bcbc30) → [`00bcbc34`](#insn-00bcbc34)
- ブロック [`00bcbc34`](#insn-00bcbc34) 範囲 `[['00bcbc34', '00bcbc37']]`
  - `FALL_THROUGH` [`00bcbc34`](#insn-00bcbc34) → [`00bcbc38`](#insn-00bcbc38)
- ブロック [`00bcbc38`](#insn-00bcbc38) 範囲 `[['00bcbc38', '00bcbc53']]`
  - `FALL_THROUGH` [`00bcbc50`](#insn-00bcbc50) → [`00bcbc54`](#insn-00bcbc54)
- ブロック [`00bcbc54`](#insn-00bcbc54) 範囲 `[['00bcbc54', '00bcbc6b']]`
  - `CONDITIONAL_JUMP` [`00bcbc68`](#insn-00bcbc68) → [`00bcbc98`](#insn-00bcbc98)
  - `FALL_THROUGH` [`00bcbc68`](#insn-00bcbc68) → [`00bcbc6c`](#insn-00bcbc6c)
- ブロック [`00bcbc6c`](#insn-00bcbc6c) 範囲 `[['00bcbc6c', '00bcbc87']]`
  - `CONDITIONAL_JUMP` [`00bcbc84`](#insn-00bcbc84) → [`00bcbc6c`](#insn-00bcbc6c)
  - `FALL_THROUGH` [`00bcbc84`](#insn-00bcbc84) → [`00bcbc88`](#insn-00bcbc88)
- ブロック [`00bcbc88`](#insn-00bcbc88) 範囲 `[['00bcbc88', '00bcbc8b']]`
  - `UNCONDITIONAL_JUMP` [`00bcbc88`](#insn-00bcbc88) → [`00bcbc98`](#insn-00bcbc98)
- ブロック [`00bcbc8c`](#insn-00bcbc8c) 範囲 `[['00bcbc8c', '00bcbc97']]`
  - `FALL_THROUGH` [`00bcbc94`](#insn-00bcbc94) → [`00bcbc98`](#insn-00bcbc98)
- ブロック [`00bcbc98`](#insn-00bcbc98) 範囲 `[['00bcbc98', '00bcbca7']]`
  - `CONDITIONAL_JUMP` [`00bcbca4`](#insn-00bcbca4) → [`00bcbc8c`](#insn-00bcbc8c)
  - `FALL_THROUGH` [`00bcbca4`](#insn-00bcbca4) → [`00bcbca8`](#insn-00bcbca8)
- ブロック [`00bcbca8`](#insn-00bcbca8) 範囲 `[['00bcbca8', '00bcbcab']]`
  - `CONDITIONAL_JUMP` [`00bcbca8`](#insn-00bcbca8) → [`00bcbcb0`](#insn-00bcbcb0)
  - `FALL_THROUGH` [`00bcbca8`](#insn-00bcbca8) → [`00bcbcac`](#insn-00bcbcac)
- ブロック [`00bcbcac`](#insn-00bcbcac) 範囲 `[['00bcbcac', '00bcbcaf']]`
  - `FALL_THROUGH` [`00bcbcac`](#insn-00bcbcac) → [`00bcbcb0`](#insn-00bcbcb0)
- ブロック [`00bcbcb0`](#insn-00bcbcb0) 範囲 `[['00bcbcb0', '00bcbcc3']]`
  - `CONDITIONAL_JUMP` [`00bcbcc0`](#insn-00bcbcc0) → [`00bcbcd4`](#insn-00bcbcd4)
  - `FALL_THROUGH` [`00bcbcc0`](#insn-00bcbcc0) → [`00bcbcc4`](#insn-00bcbcc4)
- ブロック [`00bcbcc4`](#insn-00bcbcc4) 範囲 `[['00bcbcc4', '00bcbcd3']]`
  - `FALL_THROUGH` [`00bcbcd0`](#insn-00bcbcd0) → [`00bcbcd4`](#insn-00bcbcd4)
- ブロック [`00bcbcd4`](#insn-00bcbcd4) 範囲 `[['00bcbcd4', '00bcbcd7']]`
  - `FALL_THROUGH` [`00bcbcd4`](#insn-00bcbcd4) → [`00bcbcd8`](#insn-00bcbcd8)
- ブロック [`00bcbcd8`](#insn-00bcbcd8) 範囲 `[['00bcbcd8', '00bcbcef']]`

## 命令位置別の参照

- [`00bcbacc`](#insn-00bcbacc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbad0`](#insn-00bcbad0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbad4`](#insn-00bcbad4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbae0`](#insn-00bcbae0) → `00c9ca40`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcbae8`](#insn-00bcbae8) → `011277e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth13g_auths_mutexE` · 推定型 `undefined8`
- [`00bcbaf0`](#insn-00bcbaf0) → [`00c5baa0`](../00c5b/00c5baa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baa0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbaf8`](#insn-00bcbaf8) → [`00bcbcd8`](#insn-00bcbcd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb04`](#insn-00bcbb04) → [`00c5baa0`](../00c5b/00c5baa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baa0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb18`](#insn-00bcbb18) → [`00c5bab0`](../00c5b/00c5bab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bab0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb24`](#insn-00bcbb24) → [`00c5cd80`](../00c5c/00c5cd80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cd80` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb28`](#insn-00bcbb28) → [`00bcbb3c`](#insn-00bcbb3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb34`](#insn-00bcbb34) → [`00c5ebc0`](../00c5e/00c5ebc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ebc0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb38`](#insn-00bcbb38) → [`00bcbb1c`](#insn-00bcbb1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb44`](#insn-00bcbb44) → [`00c5bc90`](../00c5b/00c5bc90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bc90` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb4c`](#insn-00bcbb4c) → [`00c5bcb0`](../00c5b/00c5bcb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bcb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb54`](#insn-00bcbb54) → `00c9ca48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcbb5c`](#insn-00bcbb5c) → `011277c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth7g_authsE` · 推定型 `undefined8`
- [`00bcbb64`](#insn-00bcbb64) → [`00bcbc54`](#insn-00bcbc54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb6c`](#insn-00bcbb6c) → [`00bcbb7c`](#insn-00bcbb7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb78`](#insn-00bcbb78) → [`00bcbc54`](#insn-00bcbc54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb84`](#insn-00bcbb84) → [`00bcbbd0`](#insn-00bcbbd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb8c`](#insn-00bcbb8c) → [`00bcbba0`](#insn-00bcbba0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb98`](#insn-00bcbb98) → [`00bcbb90`](#insn-00bcbb90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb9c`](#insn-00bcbb9c) → [`00bcbb74`](#insn-00bcbb74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbb0`](#insn-00bcbbb0) → [`00bcbb70`](#insn-00bcbb70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbc8`](#insn-00bcbbc8) → [`00bcbbb4`](#insn-00bcbbb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbcc`](#insn-00bcbbcc) → [`00bcbb74`](#insn-00bcbb74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbd8`](#insn-00bcbbd8) → `0029fc09`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcbbe0`](#insn-00bcbbe0) → [`00c5c1d0`](../00c5c/00c5c1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbe8`](#insn-00bcbbe8) → [`00bcbbfc`](#insn-00bcbbfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbf4`](#insn-00bcbbf4) → [`00bcbbec`](#insn-00bcbbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbf8`](#insn-00bcbbf8) → [`00bcbc28`](#insn-00bcbc28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc0c`](#insn-00bcbc0c) → [`00bcbc28`](#insn-00bcbc28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc24`](#insn-00bcbc24) → [`00bcbc10`](#insn-00bcbc10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc28`](#insn-00bcbc28) → `011277c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth7g_authsE` · 推定型 `undefined8`
- [`00bcbc30`](#insn-00bcbc30) → [`00bcbc38`](#insn-00bcbc38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc34`](#insn-00bcbc34) → `011277c8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth7g_authsE` · 推定型 `undefined8`
- [`00bcbc38`](#insn-00bcbc38) → `011277d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcbc38`](#insn-00bcbc38) → `011277d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcbc44`](#insn-00bcbc44) → `011277d8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcbc48`](#insn-00bcbc48) → [`00c5c670`](../00c5c/00c5c670.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c670` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc50`](#insn-00bcbc50) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc58`](#insn-00bcbc58) → `011277d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcbc68`](#insn-00bcbc68) → [`00bcbc98`](#insn-00bcbc98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc74`](#insn-00bcbc74) → [`00c5eb10`](../00c5e/00c5eb10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5eb10` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc84`](#insn-00bcbc84) → [`00bcbc6c`](#insn-00bcbc6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc88`](#insn-00bcbc88) → [`00bcbc98`](#insn-00bcbc98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc94`](#insn-00bcbc94) → [`00c5eb00`](../00c5e/00c5eb00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5eb00` · 推定シンボル `None` · 推定型 `None`
- [`00bcbca4`](#insn-00bcbca4) → [`00bcbc8c`](#insn-00bcbc8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbca8`](#insn-00bcbca8) → [`00bcbcb0`](#insn-00bcbcb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbcac`](#insn-00bcbcac) → [`00c5eac0`](../00c5e/00c5eac0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5eac0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbcb8`](#insn-00bcbcb8) → [`00c5eaf0`](../00c5e/00c5eaf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5eaf0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbcc0`](#insn-00bcbcc0) → [`00bcbcd4`](#insn-00bcbcd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbcc8`](#insn-00bcbcc8) → [`00c5eb50`](../00c5e/00c5eb50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5eb50` · 推定シンボル `None` · 推定型 `None`
- [`00bcbcd0`](#insn-00bcbcd0) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bcbcdc`](#insn-00bcbcdc) → [`00c5bab0`](../00c5b/00c5bab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bab0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbce0`](#insn-00bcbce0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbce4`](#insn-00bcbce4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbacc`](#insn-00bcbacc)

~~~json
{
  "source": "00bcbacc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbad0`](#insn-00bcbad0)

~~~json
{
  "source": "00bcbad0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbad4`](#insn-00bcbad4)

~~~json
{
  "source": "00bcbad4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbae0`](#insn-00bcbae0)

~~~json
{
  "source": "00bcbae0",
  "target": "00c9ca40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ca40",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcbae8`](#insn-00bcbae8)

~~~json
{
  "source": "00bcbae8",
  "target": "011277e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011277e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcbaf0`](#insn-00bcbaf0)

~~~json
{
  "source": "00bcbaf0",
  "target": "00c5baa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbaf8`](#insn-00bcbaf8)

~~~json
{
  "source": "00bcbaf8",
  "target": "00bcbcd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb04`](#insn-00bcbb04)

~~~json
{
  "source": "00bcbb04",
  "target": "00c5baa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbb18`](#insn-00bcbb18)

~~~json
{
  "source": "00bcbb18",
  "target": "00c5bab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbb24`](#insn-00bcbb24)

~~~json
{
  "source": "00bcbb24",
  "target": "00c5cd80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbb28`](#insn-00bcbb28)

~~~json
{
  "source": "00bcbb28",
  "target": "00bcbb3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb34`](#insn-00bcbb34)

~~~json
{
  "source": "00bcbb34",
  "target": "00c5ebc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbb38`](#insn-00bcbb38)

~~~json
{
  "source": "00bcbb38",
  "target": "00bcbb1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb44`](#insn-00bcbb44)

~~~json
{
  "source": "00bcbb44",
  "target": "00c5bc90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbb4c`](#insn-00bcbb4c)

~~~json
{
  "source": "00bcbb4c",
  "target": "00c5bcb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbb54`](#insn-00bcbb54)

~~~json
{
  "source": "00bcbb54",
  "target": "00c9ca48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ca48",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcbb5c`](#insn-00bcbb5c)

~~~json
{
  "source": "00bcbb5c",
  "target": "011277c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011277c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcbb64`](#insn-00bcbb64)

~~~json
{
  "source": "00bcbb64",
  "target": "00bcbc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb6c`](#insn-00bcbb6c)

~~~json
{
  "source": "00bcbb6c",
  "target": "00bcbb7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb78`](#insn-00bcbb78)

~~~json
{
  "source": "00bcbb78",
  "target": "00bcbc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb84`](#insn-00bcbb84)

~~~json
{
  "source": "00bcbb84",
  "target": "00bcbbd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb8c`](#insn-00bcbb8c)

~~~json
{
  "source": "00bcbb8c",
  "target": "00bcbba0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb98`](#insn-00bcbb98)

~~~json
{
  "source": "00bcbb98",
  "target": "00bcbb90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb9c`](#insn-00bcbb9c)

~~~json
{
  "source": "00bcbb9c",
  "target": "00bcbb74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbb0`](#insn-00bcbbb0)

~~~json
{
  "source": "00bcbbb0",
  "target": "00bcbb70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbc8`](#insn-00bcbbc8)

~~~json
{
  "source": "00bcbbc8",
  "target": "00bcbbb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbcc`](#insn-00bcbbcc)

~~~json
{
  "source": "00bcbbcc",
  "target": "00bcbb74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbd8`](#insn-00bcbbd8)

~~~json
{
  "source": "00bcbbd8",
  "target": "0029fc09",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029fc09",
  "offset": 0,
  "size": 28,
  "datatype": "string",
  "bytes": "44656c6574696e67204175746820257020666f722041707020257000",
  "capture_start": "0029fc09",
  "capture_bytes": 28,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcbbe0`](#insn-00bcbbe0)

~~~json
{
  "source": "00bcbbe0",
  "target": "00c5c1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbbe8`](#insn-00bcbbe8)

~~~json
{
  "source": "00bcbbe8",
  "target": "00bcbbfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbf4`](#insn-00bcbbf4)

~~~json
{
  "source": "00bcbbf4",
  "target": "00bcbbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbf8`](#insn-00bcbbf8)

~~~json
{
  "source": "00bcbbf8",
  "target": "00bcbc28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc0c`](#insn-00bcbc0c)

~~~json
{
  "source": "00bcbc0c",
  "target": "00bcbc28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc24`](#insn-00bcbc24)

~~~json
{
  "source": "00bcbc24",
  "target": "00bcbc10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc28`](#insn-00bcbc28)

~~~json
{
  "source": "00bcbc28",
  "target": "011277c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011277c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcbc30`](#insn-00bcbc30)

~~~json
{
  "source": "00bcbc30",
  "target": "00bcbc38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc34`](#insn-00bcbc34)

~~~json
{
  "source": "00bcbc34",
  "target": "011277c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011277c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcbc38`](#insn-00bcbc38)

~~~json
{
  "source": "00bcbc38",
  "target": "011277d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011277d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcbc38`](#insn-00bcbc38)

~~~json
{
  "source": "00bcbc38",
  "target": "011277d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011277d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcbc44`](#insn-00bcbc44)

~~~json
{
  "source": "00bcbc44",
  "target": "011277d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011277d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcbc48`](#insn-00bcbc48)

~~~json
{
  "source": "00bcbc48",
  "target": "00c5c670",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbc50`](#insn-00bcbc50)

~~~json
{
  "source": "00bcbc50",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbc58`](#insn-00bcbc58)

~~~json
{
  "source": "00bcbc58",
  "target": "011277d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011277d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcbc68`](#insn-00bcbc68)

~~~json
{
  "source": "00bcbc68",
  "target": "00bcbc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc74`](#insn-00bcbc74)

~~~json
{
  "source": "00bcbc74",
  "target": "00c5eb10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbc84`](#insn-00bcbc84)

~~~json
{
  "source": "00bcbc84",
  "target": "00bcbc6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc88`](#insn-00bcbc88)

~~~json
{
  "source": "00bcbc88",
  "target": "00bcbc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc94`](#insn-00bcbc94)

~~~json
{
  "source": "00bcbc94",
  "target": "00c5eb00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbca4`](#insn-00bcbca4)

~~~json
{
  "source": "00bcbca4",
  "target": "00bcbc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbca8`](#insn-00bcbca8)

~~~json
{
  "source": "00bcbca8",
  "target": "00bcbcb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbcac`](#insn-00bcbcac)

~~~json
{
  "source": "00bcbcac",
  "target": "00c5eac0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbcb8`](#insn-00bcbcb8)

~~~json
{
  "source": "00bcbcb8",
  "target": "00c5eaf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbcc0`](#insn-00bcbcc0)

~~~json
{
  "source": "00bcbcc0",
  "target": "00bcbcd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbcc8`](#insn-00bcbcc8)

~~~json
{
  "source": "00bcbcc8",
  "target": "00c5eb50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbcd0`](#insn-00bcbcd0)

~~~json
{
  "source": "00bcbcd0",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbcdc`](#insn-00bcbcdc)

~~~json
{
  "source": "00bcbcdc",
  "target": "00c5bab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbce0`](#insn-00bcbce0)

~~~json
{
  "source": "00bcbce0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbce4`](#insn-00bcbce4)

~~~json
{
  "source": "00bcbce4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
