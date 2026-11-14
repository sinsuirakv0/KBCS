# 00bcbec4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bcbec4",
  "name": "_ZN8firebase4auth4Auth20AddAuthStateListenerEPNS0_17AuthStateListenerE",
  "size": 436,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "39ca2dbe07b691bb668a63215a3f1fcff553652631c68dd0cacee5226a7e9063",
  "source_text_sha256": "39ca2dbe07b691bb668a63215a3f1fcff553652631c68dd0cacee5226a7e9063"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f80](../00c58/00c58f80.md)
- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5c0a0](../00c5c/00c5c0a0.md)
- [00c5eb90](../00c5e/00c5eb90.md)
- [00c5ebb0](../00c5e/00c5ebb0.md)

## 関連文字列（未確認候補）

~~~text
"listener_added == auth_added"
~~~

## 疑似コード / UTF-8 2525 bytes

~~~c

void _ZN8firebase4auth4Auth20AddAuthStateListenerEPNS0_17AuthStateListenerE
               (long *param_1,long *param_2)

{
  long *plVar1;
  undefined8 *puVar2;
  long lVar3;
  undefined8 *puVar4;
  long lVar5;
  bool bVar6;
  long lVar7;
  long *plVar8;
  undefined8 *puVar9;
  long *plVar10;
  long *local_58;
  long *plStack_50;
  long local_48;
  
  lVar5 = tpidr_el0;
  local_48 = *(long *)(lVar5 + 0x28);
  if (*param_1 == 0) goto LAB_00bcc04c;
  lVar3 = *param_1 + 0x268;
  _ZN8firebase5Mutex7AcquireEv(lVar3);
  lVar7 = *param_1;
  plVar10 = *(long **)(lVar7 + 0x230);
  plVar8 = *(long **)(lVar7 + 0x238);
  local_58 = param_1;
  plStack_50 = param_2;
  if ((plVar10 == plVar8) || ((long *)*plVar10 == param_2)) {
    if (plVar10 == plVar8) goto LAB_00bcbf64;
LAB_00bcbf50:
    bVar6 = false;
  }
  else {
    do {
      if (plVar8 + -1 == plVar10) goto LAB_00bcbf64;
      plVar1 = plVar10 + 1;
      plVar10 = plVar10 + 1;
    } while ((long *)*plVar1 != param_2);
    if (plVar10 != plVar8) goto LAB_00bcbf50;
LAB_00bcbf64:
    if (plVar8 == *(long **)(lVar7 + 0x240)) {
      _ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_
                (lVar7 + 0x230,&plStack_50);
    }
    else {
      *plVar8 = (long)param_2;
      *(long **)(lVar7 + 0x238) = plVar8 + 1;
    }
    bVar6 = true;
  }
  puVar9 = (undefined8 *)param_2[1];
  puVar4 = (undefined8 *)param_2[2];
  if ((puVar9 == puVar4) || ((long *)*puVar9 == local_58)) {
    if (puVar9 == puVar4) goto LAB_00bcbfe4;
LAB_00bcbfd0:
    if (bVar6) {
LAB_00bcc038:
      _ZN8firebase9LogAssertEPKcz("listener_added == auth_added");
    }
  }
  else {
    do {
      if (puVar4 + -1 == puVar9) goto LAB_00bcbfe4;
      puVar2 = puVar9 + 1;
      puVar9 = puVar9 + 1;
    } while ((long *)*puVar2 != local_58);
    if (puVar9 != puVar4) goto LAB_00bcbfd0;
LAB_00bcbfe4:
    if (puVar4 == (undefined8 *)param_2[3]) {
      _ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_
                (param_2 + 1,&local_58);
    }
    else {
      *puVar4 = local_58;
      param_2[2] = (long)(puVar4 + 1);
    }
    if (!bVar6) goto LAB_00bcc038;
    if (*(char *)(*param_1 + 0x2b9) == '\0') {
      (**(code **)(*param_2 + 0x10))(param_2,param_1);
    }
  }
  _ZN8firebase5Mutex7ReleaseEv(lVar3);
LAB_00bcc04c:
  if (*(long *)(lVar5 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
