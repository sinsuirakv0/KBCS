# 00bcaad8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcaa3c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcaa3c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-2e8fa686d4da5b664ac9d6bfa2e14a78)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bcbacc`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcbacc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-33cb128aa830b48b07e84eb5613d2130)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcaad8",
  "name": "_ZN8firebase4auth4Auth14DeleteInternalEv",
  "size": 548,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "17f9dec3d390a289091d61ddc5a115ff8bfea5642086617f2217a1896d03d297",
  "source_text_sha256": "17f9dec3d390a289091d61ddc5a115ff8bfea5642086617f2217a1896d03d297",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcaad8",
        "00bcacfb"
      ]
    ],
    "bytes_sha256": "59d6192f436fedac66ca1ecb1ba2436b23b8d55edfa1dbf9c93a40ccb3c3a89b",
    "instruction_count": 137,
    "instruction_bytes": 548,
    "body_bytes": 548,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5db00](../00c5d/00c5db00.md)

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)
- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)
- [00c5acc0](../00c5a/00c5acc0.md)
- [00c5ace0](../00c5a/00c5ace0.md)
- [00c5b200](../00c5b/00c5b200.md)
- [00c5b6a0](../00c5b/00c5b6a0.md)
- [00c5bdb0](../00c5b/00c5bdb0.md)
- [00c5daf0](../00c5d/00c5daf0.md)
- [00c5db20](../00c5d/00c5db20.md)
- [00c5db30](../00c5d/00c5db30.md)
- [00c5db40](../00c5d/00c5db40.md)
- [00c5db80](../00c5d/00c5db80.md)
- [00c5dbf0](../00c5d/00c5dbf0.md)

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
  
  uVar7 = *(undefined8 *)PTR__ZN8firebase4auth13g_auths_mutexE_00c9ba70;
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
    puVar1 = PTR__ZN8firebase4auth7g_authsE_00c9ba78;
    if (*(long **)PTR__ZN8firebase4auth7g_authsE_00c9ba78 !=
        (long *)(PTR__ZN8firebase4auth7g_authsE_00c9ba78 + 8)) {
      __ptr = *(long **)PTR__ZN8firebase4auth7g_authsE_00c9ba78;
LAB_00bcab88:
      if ((long *)__ptr[5] != param_1) goto code_r0x00bcab94;
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
LAB_00bcac60:
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
code_r0x00bcab94:
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
  if (plVar6 == (long *)(PTR__ZN8firebase4auth7g_authsE_00c9ba78 + 8)) goto LAB_00bcac60;
  goto LAB_00bcab88;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcaad8"></a> `00bcaad8` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcaadc"></a> `00bcaadc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcaae0"></a> `00bcaae0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcaae4"></a> `00bcaae4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcaae8"></a> `00bcaae8` | `88 06 00 b0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcaaec"></a> `00bcaaec` | `08 39 45 f9` | ldr x8,[x8, #0xa70] | `FALL_THROUGH`
<a id="insn-00bcaaf0"></a> `00bcaaf0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcaaf4"></a> `00bcaaf4` | `13 01 40 f9` | ldr x19,[x8] | `FALL_THROUGH`
<a id="insn-00bcaaf8"></a> `00bcaaf8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcaafc"></a> `00bcaafc` | `f5 3f 02 94` | bl 0x00c5aad0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcab00"></a> `00bcab00` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcab04"></a> `00bcab04` | `08 0f 00 b4` | cbz x8,0x00bcace4 | `CONDITIONAL_JUMP`
<a id="insn-00bcab08"></a> `00bcab08` | `15 a1 0b 91` | add x21,x8,#0x2e8 | `FALL_THROUGH`
<a id="insn-00bcab0c"></a> `00bcab0c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcab10"></a> `00bcab10` | `f0 3f 02 94` | bl 0x00c5aad0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcab14"></a> `00bcab14` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcab18"></a> `00bcab18` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcab1c"></a> `00bcab1c` | `09 91 0b 39` | strb w9,[x8, #0x2e4] | `FALL_THROUGH`
<a id="insn-00bcab20"></a> `00bcab20` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcab24"></a> `00bcab24` | `ef 3f 02 94` | bl 0x00c5aae0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcab28"></a> `00bcab28` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcab2c"></a> `00bcab2c` | `00 41 00 91` | add x0,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bcab30"></a> `00bcab30` | `a0 44 02 94` | bl 0x00c5bdb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcab34"></a> `00bcab34` | `a0 00 00 37` | tbnz w0,#0x0,0x00bcab48 | `CONDITIONAL_JUMP`
<a id="insn-00bcab38"></a> `00bcab38` | `00 d4 90 52` | mov w0,#0x86a0 | `FALL_THROUGH`
<a id="insn-00bcab3c"></a> `00bcab3c` | `20 00 a0 72` | movk w0,#0x1, LSL #16 | `FALL_THROUGH`
<a id="insn-00bcab40"></a> `00bcab40` | `2c 4c 02 94` | bl 0x00c5dbf0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcab44"></a> `00bcab44` | `f9 ff ff 17` | b 0x00bcab28 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcab48"></a> `00bcab48` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcab4c"></a> `00bcab4c` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bcab50"></a> `00bcab50` | `5c 40 02 94` | bl 0x00c5acc0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcab54"></a> `00bcab54` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcab58"></a> `00bcab58` | `62 40 02 94` | bl 0x00c5ace0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcab5c"></a> `00bcab5c` | `96 06 00 b0` | adrp x22,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcab60"></a> `00bcab60` | `d6 3e 45 f9` | ldr x22,[x22, #0xa78] | `FALL_THROUGH`
<a id="insn-00bcab64"></a> `00bcab64` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bcab68"></a> `00bcab68` | `15 85 40 f8` | ldr x21,[x8], #0x8 | `FALL_THROUGH`
<a id="insn-00bcab6c"></a> `00bcab6c` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00bcab70"></a> `00bcab70` | `80 07 00 54` | b.eq 0x00bcac60 | `CONDITIONAL_JUMP`
<a id="insn-00bcab74"></a> `00bcab74` | `c8 22 00 91` | add x8,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00bcab78"></a> `00bcab78` | `04 00 00 14` | b 0x00bcab88 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcab7c"></a> `00bcab7c` | `f5 03 0a aa` | mov x21,x10 | `FALL_THROUGH`
<a id="insn-00bcab80"></a> `00bcab80` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00bcab84"></a> `00bcab84` | `e0 06 00 54` | b.eq 0x00bcac60 | `CONDITIONAL_JUMP`
<a id="insn-00bcab88"></a> `00bcab88` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00bcab8c"></a> `00bcab8c` | `3f 01 14 eb` | cmp x9,x20 | `FALL_THROUGH`
<a id="insn-00bcab90"></a> `00bcab90` | `60 02 00 54` | b.eq 0x00bcabdc | `CONDITIONAL_JUMP`
<a id="insn-00bcab94"></a> `00bcab94` | `a9 06 40 f9` | ldr x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcab98"></a> `00bcab98` | `a9 00 00 b4` | cbz x9,0x00bcabac | `CONDITIONAL_JUMP`
<a id="insn-00bcab9c"></a> `00bcab9c` | `f5 03 09 aa` | mov x21,x9 | `FALL_THROUGH`
<a id="insn-00bcaba0"></a> `00bcaba0` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bcaba4"></a> `00bcaba4` | `c9 ff ff b5` | cbnz x9,0x00bcab9c | `CONDITIONAL_JUMP`
<a id="insn-00bcaba8"></a> `00bcaba8` | `f6 ff ff 17` | b 0x00bcab80 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcabac"></a> `00bcabac` | `e9 03 15 aa` | mov x9,x21 | `FALL_THROUGH`
<a id="insn-00bcabb0"></a> `00bcabb0` | `2a 0d 41 f8` | ldr x10,[x9, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcabb4"></a> `00bcabb4` | `4b 01 40 f9` | ldr x11,[x10] | `FALL_THROUGH`
<a id="insn-00bcabb8"></a> `00bcabb8` | `7f 01 15 eb` | cmp x11,x21 | `FALL_THROUGH`
<a id="insn-00bcabbc"></a> `00bcabbc` | `00 fe ff 54` | b.eq 0x00bcab7c | `CONDITIONAL_JUMP`
<a id="insn-00bcabc0"></a> `00bcabc0` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00bcabc4"></a> `00bcabc4` | `e9 03 0a aa` | mov x9,x10 | `FALL_THROUGH`
<a id="insn-00bcabc8"></a> `00bcabc8` | `35 0d 41 f8` | ldr x21,[x9, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcabcc"></a> `00bcabcc` | `ab 02 40 f9` | ldr x11,[x21] | `FALL_THROUGH`
<a id="insn-00bcabd0"></a> `00bcabd0` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcabd4"></a> `00bcabd4` | `61 ff ff 54` | b.ne 0x00bcabc0 | `CONDITIONAL_JUMP`
<a id="insn-00bcabd8"></a> `00bcabd8` | `ea ff ff 17` | b 0x00bcab80 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcabdc"></a> `00bcabdc` | `a2 12 40 f9` | ldr x2,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00bcabe0"></a> `00bcabe0` | `a0 b6 ff b0` | adrp x0,0x29f000 | `FALL_THROUGH`
<a id="insn-00bcabe4"></a> `00bcabe4` | `00 24 2f 91` | add x0,x0,#0xbc9 | `FALL_THROUGH`
<a id="insn-00bcabe8"></a> `00bcabe8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcabec"></a> `00bcabec` | `85 41 02 94` | bl 0x00c5b200 | `UNCONDITIONAL_CALL`
<a id="insn-00bcabf0"></a> `00bcabf0` | `a9 06 40 f9` | ldr x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcabf4"></a> `00bcabf4` | `a9 00 00 b4` | cbz x9,0x00bcac08 | `CONDITIONAL_JUMP`
<a id="insn-00bcabf8"></a> `00bcabf8` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00bcabfc"></a> `00bcabfc` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bcac00"></a> `00bcac00` | `c9 ff ff b5` | cbnz x9,0x00bcabf8 | `CONDITIONAL_JUMP`
<a id="insn-00bcac04"></a> `00bcac04` | `0c 00 00 14` | b 0x00bcac34 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcac08"></a> `00bcac08` | `e9 03 15 aa` | mov x9,x21 | `FALL_THROUGH`
<a id="insn-00bcac0c"></a> `00bcac0c` | `28 0d 41 f8` | ldr x8,[x9, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcac10"></a> `00bcac10` | `0a 01 40 f9` | ldr x10,[x8] | `FALL_THROUGH`
<a id="insn-00bcac14"></a> `00bcac14` | `5f 01 15 eb` | cmp x10,x21 | `FALL_THROUGH`
<a id="insn-00bcac18"></a> `00bcac18` | `e0 00 00 54` | b.eq 0x00bcac34 | `CONDITIONAL_JUMP`
<a id="insn-00bcac1c"></a> `00bcac1c` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00bcac20"></a> `00bcac20` | `e9 03 0a aa` | mov x9,x10 | `FALL_THROUGH`
<a id="insn-00bcac24"></a> `00bcac24` | `28 0d 41 f8` | ldr x8,[x9, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcac28"></a> `00bcac28` | `0b 01 40 f9` | ldr x11,[x8] | `FALL_THROUGH`
<a id="insn-00bcac2c"></a> `00bcac2c` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcac30"></a> `00bcac30` | `61 ff ff 54` | b.ne 0x00bcac1c | `CONDITIONAL_JUMP`
<a id="insn-00bcac34"></a> `00bcac34` | `c9 02 40 f9` | ldr x9,[x22] | `FALL_THROUGH`
<a id="insn-00bcac38"></a> `00bcac38` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bcac3c"></a> `00bcac3c` | `41 00 00 54` | b.ne 0x00bcac44 | `CONDITIONAL_JUMP`
<a id="insn-00bcac40"></a> `00bcac40` | `c8 02 00 f9` | str x8,[x22] | `FALL_THROUGH`
<a id="insn-00bcac44"></a> `00bcac44` | `c0 a2 40 a9` | ldp x0,x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bcac48"></a> `00bcac48` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bcac4c"></a> `00bcac4c` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcac50"></a> `00bcac50` | `c8 0a 00 f9` | str x8,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00bcac54"></a> `00bcac54` | `93 42 02 94` | bl 0x00c5b6a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcac58"></a> `00bcac58` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcac5c"></a> `00bcac5c` | `c9 34 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bcac60"></a> `00bcac60` | `95 02 40 f9` | ldr x21,[x20] | `FALL_THROUGH`
<a id="insn-00bcac64"></a> `00bcac64` | `d6 0a 40 f9` | ldr x22,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00bcac68"></a> `00bcac68` | `a9 1a 41 f9` | ldr x9,[x21, #0x230] | `FALL_THROUGH`
<a id="insn-00bcac6c"></a> `00bcac6c` | `a8 1e 41 f9` | ldr x8,[x21, #0x238] | `FALL_THROUGH`
<a id="insn-00bcac70"></a> `00bcac70` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcac74"></a> `00bcac74` | `80 01 00 54` | b.eq 0x00bcaca4 | `CONDITIONAL_JUMP`
<a id="insn-00bcac78"></a> `00bcac78` | `a0 06 40 f9` | ldr x0,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcac7c"></a> `00bcac7c` | `01 81 5f f8` | ldur x1,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00bcac80"></a> `00bcac80` | `b0 4b 02 94` | bl 0x00c5db40 | `UNCONDITIONAL_CALL`
<a id="insn-00bcac84"></a> `00bcac84` | `a9 1a 41 f9` | ldr x9,[x21, #0x230] | `FALL_THROUGH`
<a id="insn-00bcac88"></a> `00bcac88` | `a8 1e 41 f9` | ldr x8,[x21, #0x238] | `FALL_THROUGH`
<a id="insn-00bcac8c"></a> `00bcac8c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcac90"></a> `00bcac90` | `41 ff ff 54` | b.ne 0x00bcac78 | `CONDITIONAL_JUMP`
<a id="insn-00bcac94"></a> `00bcac94` | `04 00 00 14` | b 0x00bcaca4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcac98"></a> `00bcac98` | `a0 06 40 f9` | ldr x0,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcac9c"></a> `00bcac9c` | `01 81 5f f8` | ldur x1,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00bcaca0"></a> `00bcaca0` | `a4 4b 02 94` | bl 0x00c5db30 | `UNCONDITIONAL_CALL`
<a id="insn-00bcaca4"></a> `00bcaca4` | `a9 26 41 f9` | ldr x9,[x21, #0x248] | `FALL_THROUGH`
<a id="insn-00bcaca8"></a> `00bcaca8` | `a8 2a 41 f9` | ldr x8,[x21, #0x250] | `FALL_THROUGH`
<a id="insn-00bcacac"></a> `00bcacac` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcacb0"></a> `00bcacb0` | `41 ff ff 54` | b.ne 0x00bcac98 | `CONDITIONAL_JUMP`
<a id="insn-00bcacb4"></a> `00bcacb4` | `56 00 00 35` | cbnz w22,0x00bcacbc | `CONDITIONAL_JUMP`
<a id="insn-00bcacb8"></a> `00bcacb8` | `8e 4b 02 94` | bl 0x00c5daf0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcacbc"></a> `00bcacbc` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00bcacc0"></a> `00bcacc0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcacc4"></a> `00bcacc4` | `97 4b 02 94` | bl 0x00c5db20 | `UNCONDITIONAL_CALL`
<a id="insn-00bcacc8"></a> `00bcacc8` | `95 02 40 f9` | ldr x21,[x20] | `FALL_THROUGH`
<a id="insn-00bcaccc"></a> `00bcaccc` | `b5 00 00 b4` | cbz x21,0x00bcace0 | `CONDITIONAL_JUMP`
<a id="insn-00bcacd0"></a> `00bcacd0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcacd4"></a> `00bcacd4` | `ab 4b 02 94` | bl 0x00c5db80 | `UNCONDITIONAL_CALL`
<a id="insn-00bcacd8"></a> `00bcacd8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcacdc"></a> `00bcacdc` | `a9 34 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bcace0"></a> `00bcace0` | `9f 02 00 f9` | str xzr,[x20] | `FALL_THROUGH`
<a id="insn-00bcace4"></a> `00bcace4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcace8"></a> `00bcace8` | `7e 3f 02 94` | bl 0x00c5aae0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcacec"></a> `00bcacec` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcacf0"></a> `00bcacf0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcacf4"></a> `00bcacf4` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcacf8"></a> `00bcacf8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcaad8`](#insn-00bcaad8) 範囲 `[['00bcaad8', '00bcab07']]`
  - `CONDITIONAL_JUMP` [`00bcab04`](#insn-00bcab04) → [`00bcace4`](#insn-00bcace4)
  - `FALL_THROUGH` [`00bcab04`](#insn-00bcab04) → [`00bcab08`](#insn-00bcab08)
- ブロック [`00bcab08`](#insn-00bcab08) 範囲 `[['00bcab08', '00bcab27']]`
  - `FALL_THROUGH` [`00bcab24`](#insn-00bcab24) → [`00bcab28`](#insn-00bcab28)
- ブロック [`00bcab28`](#insn-00bcab28) 範囲 `[['00bcab28', '00bcab37']]`
  - `CONDITIONAL_JUMP` [`00bcab34`](#insn-00bcab34) → [`00bcab48`](#insn-00bcab48)
  - `FALL_THROUGH` [`00bcab34`](#insn-00bcab34) → [`00bcab38`](#insn-00bcab38)
- ブロック [`00bcab38`](#insn-00bcab38) 範囲 `[['00bcab38', '00bcab47']]`
  - `UNCONDITIONAL_JUMP` [`00bcab44`](#insn-00bcab44) → [`00bcab28`](#insn-00bcab28)
- ブロック [`00bcab48`](#insn-00bcab48) 範囲 `[['00bcab48', '00bcab73']]`
  - `CONDITIONAL_JUMP` [`00bcab70`](#insn-00bcab70) → [`00bcac60`](#insn-00bcac60)
  - `FALL_THROUGH` [`00bcab70`](#insn-00bcab70) → [`00bcab74`](#insn-00bcab74)
- ブロック [`00bcab74`](#insn-00bcab74) 範囲 `[['00bcab74', '00bcab7b']]`
  - `UNCONDITIONAL_JUMP` [`00bcab78`](#insn-00bcab78) → [`00bcab88`](#insn-00bcab88)
- ブロック [`00bcab7c`](#insn-00bcab7c) 範囲 `[['00bcab7c', '00bcab7f']]`
  - `FALL_THROUGH` [`00bcab7c`](#insn-00bcab7c) → [`00bcab80`](#insn-00bcab80)
- ブロック [`00bcab80`](#insn-00bcab80) 範囲 `[['00bcab80', '00bcab87']]`
  - `CONDITIONAL_JUMP` [`00bcab84`](#insn-00bcab84) → [`00bcac60`](#insn-00bcac60)
  - `FALL_THROUGH` [`00bcab84`](#insn-00bcab84) → [`00bcab88`](#insn-00bcab88)
- ブロック [`00bcab88`](#insn-00bcab88) 範囲 `[['00bcab88', '00bcab93']]`
  - `CONDITIONAL_JUMP` [`00bcab90`](#insn-00bcab90) → [`00bcabdc`](#insn-00bcabdc)
  - `FALL_THROUGH` [`00bcab90`](#insn-00bcab90) → [`00bcab94`](#insn-00bcab94)
- ブロック [`00bcab94`](#insn-00bcab94) 範囲 `[['00bcab94', '00bcab9b']]`
  - `CONDITIONAL_JUMP` [`00bcab98`](#insn-00bcab98) → [`00bcabac`](#insn-00bcabac)
  - `FALL_THROUGH` [`00bcab98`](#insn-00bcab98) → [`00bcab9c`](#insn-00bcab9c)
- ブロック [`00bcab9c`](#insn-00bcab9c) 範囲 `[['00bcab9c', '00bcaba7']]`
  - `CONDITIONAL_JUMP` [`00bcaba4`](#insn-00bcaba4) → [`00bcab9c`](#insn-00bcab9c)
  - `FALL_THROUGH` [`00bcaba4`](#insn-00bcaba4) → [`00bcaba8`](#insn-00bcaba8)
- ブロック [`00bcaba8`](#insn-00bcaba8) 範囲 `[['00bcaba8', '00bcabab']]`
  - `UNCONDITIONAL_JUMP` [`00bcaba8`](#insn-00bcaba8) → [`00bcab80`](#insn-00bcab80)
- ブロック [`00bcabac`](#insn-00bcabac) 範囲 `[['00bcabac', '00bcabbf']]`
  - `CONDITIONAL_JUMP` [`00bcabbc`](#insn-00bcabbc) → [`00bcab7c`](#insn-00bcab7c)
  - `FALL_THROUGH` [`00bcabbc`](#insn-00bcabbc) → [`00bcabc0`](#insn-00bcabc0)
- ブロック [`00bcabc0`](#insn-00bcabc0) 範囲 `[['00bcabc0', '00bcabd7']]`
  - `CONDITIONAL_JUMP` [`00bcabd4`](#insn-00bcabd4) → [`00bcabc0`](#insn-00bcabc0)
  - `FALL_THROUGH` [`00bcabd4`](#insn-00bcabd4) → [`00bcabd8`](#insn-00bcabd8)
- ブロック [`00bcabd8`](#insn-00bcabd8) 範囲 `[['00bcabd8', '00bcabdb']]`
  - `UNCONDITIONAL_JUMP` [`00bcabd8`](#insn-00bcabd8) → [`00bcab80`](#insn-00bcab80)
- ブロック [`00bcabdc`](#insn-00bcabdc) 範囲 `[['00bcabdc', '00bcabf7']]`
  - `CONDITIONAL_JUMP` [`00bcabf4`](#insn-00bcabf4) → [`00bcac08`](#insn-00bcac08)
  - `FALL_THROUGH` [`00bcabf4`](#insn-00bcabf4) → [`00bcabf8`](#insn-00bcabf8)
- ブロック [`00bcabf8`](#insn-00bcabf8) 範囲 `[['00bcabf8', '00bcac03']]`
  - `CONDITIONAL_JUMP` [`00bcac00`](#insn-00bcac00) → [`00bcabf8`](#insn-00bcabf8)
  - `FALL_THROUGH` [`00bcac00`](#insn-00bcac00) → [`00bcac04`](#insn-00bcac04)
- ブロック [`00bcac04`](#insn-00bcac04) 範囲 `[['00bcac04', '00bcac07']]`
  - `UNCONDITIONAL_JUMP` [`00bcac04`](#insn-00bcac04) → [`00bcac34`](#insn-00bcac34)
- ブロック [`00bcac08`](#insn-00bcac08) 範囲 `[['00bcac08', '00bcac1b']]`
  - `CONDITIONAL_JUMP` [`00bcac18`](#insn-00bcac18) → [`00bcac34`](#insn-00bcac34)
  - `FALL_THROUGH` [`00bcac18`](#insn-00bcac18) → [`00bcac1c`](#insn-00bcac1c)
- ブロック [`00bcac1c`](#insn-00bcac1c) 範囲 `[['00bcac1c', '00bcac33']]`
  - `CONDITIONAL_JUMP` [`00bcac30`](#insn-00bcac30) → [`00bcac1c`](#insn-00bcac1c)
  - `FALL_THROUGH` [`00bcac30`](#insn-00bcac30) → [`00bcac34`](#insn-00bcac34)
- ブロック [`00bcac34`](#insn-00bcac34) 範囲 `[['00bcac34', '00bcac3f']]`
  - `CONDITIONAL_JUMP` [`00bcac3c`](#insn-00bcac3c) → [`00bcac44`](#insn-00bcac44)
  - `FALL_THROUGH` [`00bcac3c`](#insn-00bcac3c) → [`00bcac40`](#insn-00bcac40)
- ブロック [`00bcac40`](#insn-00bcac40) 範囲 `[['00bcac40', '00bcac43']]`
  - `FALL_THROUGH` [`00bcac40`](#insn-00bcac40) → [`00bcac44`](#insn-00bcac44)
- ブロック [`00bcac44`](#insn-00bcac44) 範囲 `[['00bcac44', '00bcac5f']]`
  - `FALL_THROUGH` [`00bcac5c`](#insn-00bcac5c) → [`00bcac60`](#insn-00bcac60)
- ブロック [`00bcac60`](#insn-00bcac60) 範囲 `[['00bcac60', '00bcac77']]`
  - `CONDITIONAL_JUMP` [`00bcac74`](#insn-00bcac74) → [`00bcaca4`](#insn-00bcaca4)
  - `FALL_THROUGH` [`00bcac74`](#insn-00bcac74) → [`00bcac78`](#insn-00bcac78)
- ブロック [`00bcac78`](#insn-00bcac78) 範囲 `[['00bcac78', '00bcac93']]`
  - `CONDITIONAL_JUMP` [`00bcac90`](#insn-00bcac90) → [`00bcac78`](#insn-00bcac78)
  - `FALL_THROUGH` [`00bcac90`](#insn-00bcac90) → [`00bcac94`](#insn-00bcac94)
- ブロック [`00bcac94`](#insn-00bcac94) 範囲 `[['00bcac94', '00bcac97']]`
  - `UNCONDITIONAL_JUMP` [`00bcac94`](#insn-00bcac94) → [`00bcaca4`](#insn-00bcaca4)
- ブロック [`00bcac98`](#insn-00bcac98) 範囲 `[['00bcac98', '00bcaca3']]`
  - `FALL_THROUGH` [`00bcaca0`](#insn-00bcaca0) → [`00bcaca4`](#insn-00bcaca4)
- ブロック [`00bcaca4`](#insn-00bcaca4) 範囲 `[['00bcaca4', '00bcacb3']]`
  - `CONDITIONAL_JUMP` [`00bcacb0`](#insn-00bcacb0) → [`00bcac98`](#insn-00bcac98)
  - `FALL_THROUGH` [`00bcacb0`](#insn-00bcacb0) → [`00bcacb4`](#insn-00bcacb4)
- ブロック [`00bcacb4`](#insn-00bcacb4) 範囲 `[['00bcacb4', '00bcacb7']]`
  - `CONDITIONAL_JUMP` [`00bcacb4`](#insn-00bcacb4) → [`00bcacbc`](#insn-00bcacbc)
  - `FALL_THROUGH` [`00bcacb4`](#insn-00bcacb4) → [`00bcacb8`](#insn-00bcacb8)
- ブロック [`00bcacb8`](#insn-00bcacb8) 範囲 `[['00bcacb8', '00bcacbb']]`
  - `FALL_THROUGH` [`00bcacb8`](#insn-00bcacb8) → [`00bcacbc`](#insn-00bcacbc)
- ブロック [`00bcacbc`](#insn-00bcacbc) 範囲 `[['00bcacbc', '00bcaccf']]`
  - `CONDITIONAL_JUMP` [`00bcaccc`](#insn-00bcaccc) → [`00bcace0`](#insn-00bcace0)
  - `FALL_THROUGH` [`00bcaccc`](#insn-00bcaccc) → [`00bcacd0`](#insn-00bcacd0)
- ブロック [`00bcacd0`](#insn-00bcacd0) 範囲 `[['00bcacd0', '00bcacdf']]`
  - `FALL_THROUGH` [`00bcacdc`](#insn-00bcacdc) → [`00bcace0`](#insn-00bcace0)
- ブロック [`00bcace0`](#insn-00bcace0) 範囲 `[['00bcace0', '00bcace3']]`
  - `FALL_THROUGH` [`00bcace0`](#insn-00bcace0) → [`00bcace4`](#insn-00bcace4)
- ブロック [`00bcace4`](#insn-00bcace4) 範囲 `[['00bcace4', '00bcacfb']]`

## 命令位置別の参照

- [`00bcaad8`](#insn-00bcaad8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaadc`](#insn-00bcaadc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaae0`](#insn-00bcaae0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaaec`](#insn-00bcaaec) → `00c9ba70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcaaf4`](#insn-00bcaaf4) → `01126820`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth13g_auths_mutexE` · 推定型 `undefined8`
- [`00bcaafc`](#insn-00bcaafc) → [`00c5aad0`](../00c5a/00c5aad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aad0` · 推定シンボル `None` · 推定型 `None`
- [`00bcab04`](#insn-00bcab04) → [`00bcace4`](#insn-00bcace4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab10`](#insn-00bcab10) → [`00c5aad0`](../00c5a/00c5aad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aad0` · 推定シンボル `None` · 推定型 `None`
- [`00bcab24`](#insn-00bcab24) → [`00c5aae0`](../00c5a/00c5aae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aae0` · 推定シンボル `None` · 推定型 `None`
- [`00bcab30`](#insn-00bcab30) → [`00c5bdb0`](../00c5b/00c5bdb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bdb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcab34`](#insn-00bcab34) → [`00bcab48`](#insn-00bcab48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab40`](#insn-00bcab40) → [`00c5dbf0`](../00c5d/00c5dbf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dbf0` · 推定シンボル `None` · 推定型 `None`
- [`00bcab44`](#insn-00bcab44) → [`00bcab28`](#insn-00bcab28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab50`](#insn-00bcab50) → [`00c5acc0`](../00c5a/00c5acc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5acc0` · 推定シンボル `None` · 推定型 `None`
- [`00bcab58`](#insn-00bcab58) → [`00c5ace0`](../00c5a/00c5ace0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ace0` · 推定シンボル `None` · 推定型 `None`
- [`00bcab60`](#insn-00bcab60) → `00c9ba78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcab68`](#insn-00bcab68) → `01126808`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth7g_authsE` · 推定型 `undefined8`
- [`00bcab70`](#insn-00bcab70) → [`00bcac60`](#insn-00bcac60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab78`](#insn-00bcab78) → [`00bcab88`](#insn-00bcab88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab84`](#insn-00bcab84) → [`00bcac60`](#insn-00bcac60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab90`](#insn-00bcab90) → [`00bcabdc`](#insn-00bcabdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab98`](#insn-00bcab98) → [`00bcabac`](#insn-00bcabac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaba4`](#insn-00bcaba4) → [`00bcab9c`](#insn-00bcab9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaba8`](#insn-00bcaba8) → [`00bcab80`](#insn-00bcab80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcabbc`](#insn-00bcabbc) → [`00bcab7c`](#insn-00bcab7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcabd4`](#insn-00bcabd4) → [`00bcabc0`](#insn-00bcabc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcabd8`](#insn-00bcabd8) → [`00bcab80`](#insn-00bcab80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcabe4`](#insn-00bcabe4) → `0029fbc9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcabec`](#insn-00bcabec) → [`00c5b200`](../00c5b/00c5b200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b200` · 推定シンボル `None` · 推定型 `None`
- [`00bcabf4`](#insn-00bcabf4) → [`00bcac08`](#insn-00bcac08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac00`](#insn-00bcac00) → [`00bcabf8`](#insn-00bcabf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac04`](#insn-00bcac04) → [`00bcac34`](#insn-00bcac34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac18`](#insn-00bcac18) → [`00bcac34`](#insn-00bcac34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac30`](#insn-00bcac30) → [`00bcac1c`](#insn-00bcac1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac34`](#insn-00bcac34) → `01126808`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth7g_authsE` · 推定型 `undefined8`
- [`00bcac3c`](#insn-00bcac3c) → [`00bcac44`](#insn-00bcac44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac40`](#insn-00bcac40) → `01126808`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth7g_authsE` · 推定型 `undefined8`
- [`00bcac44`](#insn-00bcac44) → `01126810`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcac44`](#insn-00bcac44) → `01126818`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcac50`](#insn-00bcac50) → `01126818`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcac54`](#insn-00bcac54) → [`00c5b6a0`](../00c5b/00c5b6a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b6a0` · 推定シンボル `None` · 推定型 `None`
- [`00bcac5c`](#insn-00bcac5c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bcac64`](#insn-00bcac64) → `01126818`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcac74`](#insn-00bcac74) → [`00bcaca4`](#insn-00bcaca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac80`](#insn-00bcac80) → [`00c5db40`](../00c5d/00c5db40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5db40` · 推定シンボル `None` · 推定型 `None`
- [`00bcac90`](#insn-00bcac90) → [`00bcac78`](#insn-00bcac78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac94`](#insn-00bcac94) → [`00bcaca4`](#insn-00bcaca4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaca0`](#insn-00bcaca0) → [`00c5db30`](../00c5d/00c5db30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5db30` · 推定シンボル `None` · 推定型 `None`
- [`00bcacb0`](#insn-00bcacb0) → [`00bcac98`](#insn-00bcac98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcacb4`](#insn-00bcacb4) → [`00bcacbc`](#insn-00bcacbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcacb8`](#insn-00bcacb8) → [`00c5daf0`](../00c5d/00c5daf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5daf0` · 推定シンボル `None` · 推定型 `None`
- [`00bcacc4`](#insn-00bcacc4) → [`00c5db20`](../00c5d/00c5db20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5db20` · 推定シンボル `None` · 推定型 `None`
- [`00bcaccc`](#insn-00bcaccc) → [`00bcace0`](#insn-00bcace0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcacd4`](#insn-00bcacd4) → [`00c5db80`](../00c5d/00c5db80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5db80` · 推定シンボル `None` · 推定型 `None`
- [`00bcacdc`](#insn-00bcacdc) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bcace8`](#insn-00bcace8) → [`00c5aae0`](../00c5a/00c5aae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aae0` · 推定シンボル `None` · 推定型 `None`
- [`00bcacec`](#insn-00bcacec) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcacf0`](#insn-00bcacf0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcaad8`](#insn-00bcaad8)

~~~json
{
  "source": "00bcaad8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaadc`](#insn-00bcaadc)

~~~json
{
  "source": "00bcaadc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaae0`](#insn-00bcaae0)

~~~json
{
  "source": "00bcaae0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaaec`](#insn-00bcaaec)

~~~json
{
  "source": "00bcaaec",
  "target": "00c9ba70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ba70",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcaaf4`](#insn-00bcaaf4)

~~~json
{
  "source": "00bcaaf4",
  "target": "01126820",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126820",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcaafc`](#insn-00bcaafc)

~~~json
{
  "source": "00bcaafc",
  "target": "00c5aad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcab04`](#insn-00bcab04)

~~~json
{
  "source": "00bcab04",
  "target": "00bcace4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab10`](#insn-00bcab10)

~~~json
{
  "source": "00bcab10",
  "target": "00c5aad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcab24`](#insn-00bcab24)

~~~json
{
  "source": "00bcab24",
  "target": "00c5aae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcab30`](#insn-00bcab30)

~~~json
{
  "source": "00bcab30",
  "target": "00c5bdb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcab34`](#insn-00bcab34)

~~~json
{
  "source": "00bcab34",
  "target": "00bcab48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab40`](#insn-00bcab40)

~~~json
{
  "source": "00bcab40",
  "target": "00c5dbf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcab44`](#insn-00bcab44)

~~~json
{
  "source": "00bcab44",
  "target": "00bcab28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab50`](#insn-00bcab50)

~~~json
{
  "source": "00bcab50",
  "target": "00c5acc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcab58`](#insn-00bcab58)

~~~json
{
  "source": "00bcab58",
  "target": "00c5ace0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcab60`](#insn-00bcab60)

~~~json
{
  "source": "00bcab60",
  "target": "00c9ba78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ba78",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcab68`](#insn-00bcab68)

~~~json
{
  "source": "00bcab68",
  "target": "01126808",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126808",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcab70`](#insn-00bcab70)

~~~json
{
  "source": "00bcab70",
  "target": "00bcac60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab78`](#insn-00bcab78)

~~~json
{
  "source": "00bcab78",
  "target": "00bcab88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab84`](#insn-00bcab84)

~~~json
{
  "source": "00bcab84",
  "target": "00bcac60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab90`](#insn-00bcab90)

~~~json
{
  "source": "00bcab90",
  "target": "00bcabdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab98`](#insn-00bcab98)

~~~json
{
  "source": "00bcab98",
  "target": "00bcabac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaba4`](#insn-00bcaba4)

~~~json
{
  "source": "00bcaba4",
  "target": "00bcab9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaba8`](#insn-00bcaba8)

~~~json
{
  "source": "00bcaba8",
  "target": "00bcab80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcabbc`](#insn-00bcabbc)

~~~json
{
  "source": "00bcabbc",
  "target": "00bcab7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcabd4`](#insn-00bcabd4)

~~~json
{
  "source": "00bcabd4",
  "target": "00bcabc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcabd8`](#insn-00bcabd8)

~~~json
{
  "source": "00bcabd8",
  "target": "00bcab80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcabe4`](#insn-00bcabe4)

~~~json
{
  "source": "00bcabe4",
  "target": "0029fbc9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029fbc9",
  "offset": 0,
  "size": 28,
  "datatype": "string",
  "bytes": "44656c6574696e67204175746820257020666f722041707020257000",
  "capture_start": "0029fbc9",
  "capture_bytes": 28,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcabec`](#insn-00bcabec)

~~~json
{
  "source": "00bcabec",
  "target": "00c5b200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcabf4`](#insn-00bcabf4)

~~~json
{
  "source": "00bcabf4",
  "target": "00bcac08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac00`](#insn-00bcac00)

~~~json
{
  "source": "00bcac00",
  "target": "00bcabf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac04`](#insn-00bcac04)

~~~json
{
  "source": "00bcac04",
  "target": "00bcac34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac18`](#insn-00bcac18)

~~~json
{
  "source": "00bcac18",
  "target": "00bcac34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac30`](#insn-00bcac30)

~~~json
{
  "source": "00bcac30",
  "target": "00bcac1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac34`](#insn-00bcac34)

~~~json
{
  "source": "00bcac34",
  "target": "01126808",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126808",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcac3c`](#insn-00bcac3c)

~~~json
{
  "source": "00bcac3c",
  "target": "00bcac44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac40`](#insn-00bcac40)

~~~json
{
  "source": "00bcac40",
  "target": "01126808",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126808",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcac44`](#insn-00bcac44)

~~~json
{
  "source": "00bcac44",
  "target": "01126810",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126810",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcac44`](#insn-00bcac44)

~~~json
{
  "source": "00bcac44",
  "target": "01126818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126818",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcac50`](#insn-00bcac50)

~~~json
{
  "source": "00bcac50",
  "target": "01126818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126818",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcac54`](#insn-00bcac54)

~~~json
{
  "source": "00bcac54",
  "target": "00c5b6a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcac5c`](#insn-00bcac5c)

~~~json
{
  "source": "00bcac5c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcac64`](#insn-00bcac64)

~~~json
{
  "source": "00bcac64",
  "target": "01126818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126818",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcac74`](#insn-00bcac74)

~~~json
{
  "source": "00bcac74",
  "target": "00bcaca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac80`](#insn-00bcac80)

~~~json
{
  "source": "00bcac80",
  "target": "00c5db40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcac90`](#insn-00bcac90)

~~~json
{
  "source": "00bcac90",
  "target": "00bcac78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac94`](#insn-00bcac94)

~~~json
{
  "source": "00bcac94",
  "target": "00bcaca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaca0`](#insn-00bcaca0)

~~~json
{
  "source": "00bcaca0",
  "target": "00c5db30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcacb0`](#insn-00bcacb0)

~~~json
{
  "source": "00bcacb0",
  "target": "00bcac98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcacb4`](#insn-00bcacb4)

~~~json
{
  "source": "00bcacb4",
  "target": "00bcacbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcacb8`](#insn-00bcacb8)

~~~json
{
  "source": "00bcacb8",
  "target": "00c5daf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcacc4`](#insn-00bcacc4)

~~~json
{
  "source": "00bcacc4",
  "target": "00c5db20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcaccc`](#insn-00bcaccc)

~~~json
{
  "source": "00bcaccc",
  "target": "00bcace0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcacd4`](#insn-00bcacd4)

~~~json
{
  "source": "00bcacd4",
  "target": "00c5db80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcacdc`](#insn-00bcacdc)

~~~json
{
  "source": "00bcacdc",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcace8`](#insn-00bcace8)

~~~json
{
  "source": "00bcace8",
  "target": "00c5aae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcacec`](#insn-00bcacec)

~~~json
{
  "source": "00bcacec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcacf0`](#insn-00bcacf0)

~~~json
{
  "source": "00bcacf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
