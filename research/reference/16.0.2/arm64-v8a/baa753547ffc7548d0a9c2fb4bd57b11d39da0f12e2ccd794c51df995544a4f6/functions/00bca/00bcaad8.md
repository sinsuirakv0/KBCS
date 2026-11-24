# 00bcaad8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcaa3c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcaa3c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0081.md#compare-2e8fa686d4da5b664ac9d6bfa2e14a78)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0093.md#compare-33cb128aa830b48b07e84eb5613d2130)
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
  "source_text_sha256": "17f9dec3d390a289091d61ddc5a115ff8bfea5642086617f2217a1896d03d297"
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
