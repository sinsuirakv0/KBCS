# 00bcabdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bcabdc",
  "name": "_ZN8firebase4auth4Auth18AddIdTokenListenerEPNS0_15IdTokenListenerE",
  "size": 444,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a80823bf55d0e2dbc21b7ff941933b87a91f6f001da373ad23dc18375a591e25",
  "source_text_sha256": "a80823bf55d0e2dbc21b7ff941933b87a91f6f001da373ad23dc18375a591e25"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5d5e0](../00c5d/00c5d5e0.md)
- [00c5d6d0](../00c5d/00c5d6d0.md)
- [00c5d710](../00c5d/00c5d710.md)

## 関連文字列（未確認候補）

~~~text
"listener_added == auth_added"
~~~

## 疑似コード / UTF-8 2614 bytes

~~~c

void _ZN8firebase4auth4Auth18AddIdTokenListenerEPNS0_15IdTokenListenerE(long *param_1,long *param_2)

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
  if (*param_1 == 0) goto LAB_00bcad6c;
  lVar3 = *param_1 + 0x268;
  _ZN8firebase5Mutex7AcquireEv(lVar3);
  lVar7 = *param_1;
  plVar10 = *(long **)(lVar7 + 0x248);
  plVar8 = *(long **)(lVar7 + 0x250);
  local_58 = param_1;
  plStack_50 = param_2;
  if ((plVar10 == plVar8) || ((long *)*plVar10 == param_2)) {
    if (plVar10 == plVar8) goto LAB_00bcac7c;
LAB_00bcac68:
    bVar6 = false;
  }
  else {
    do {
      if (plVar8 + -1 == plVar10) goto LAB_00bcac7c;
      plVar1 = plVar10 + 1;
      plVar10 = plVar10 + 1;
    } while ((long *)*plVar1 != param_2);
    if (plVar10 != plVar8) goto LAB_00bcac68;
LAB_00bcac7c:
    if (plVar8 == *(long **)(lVar7 + 600)) {
      _ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_
                (lVar7 + 0x248,&plStack_50);
    }
    else {
      *plVar8 = (long)param_2;
      *(long **)(lVar7 + 0x250) = plVar8 + 1;
    }
    bVar6 = true;
  }
  puVar9 = (undefined8 *)param_2[1];
  puVar4 = (undefined8 *)param_2[2];
  if ((puVar9 == puVar4) || ((long *)*puVar9 == local_58)) {
    if (puVar9 == puVar4) goto LAB_00bcacfc;
LAB_00bcace8:
    if (bVar6) {
LAB_00bcad58:
      _ZN8firebase9LogAssertEPKcz("listener_added == auth_added");
    }
  }
  else {
    do {
      if (puVar4 + -1 == puVar9) goto LAB_00bcacfc;
      puVar2 = puVar9 + 1;
      puVar9 = puVar9 + 1;
    } while ((long *)*puVar2 != local_58);
    if (puVar9 != puVar4) goto LAB_00bcace8;
LAB_00bcacfc:
    if (puVar4 == (undefined8 *)param_2[3]) {
      _ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_
                (param_2 + 1,&local_58);
    }
    else {
      *puVar4 = local_58;
      param_2[2] = (long)(puVar4 + 1);
    }
    if (!bVar6) goto LAB_00bcad58;
    lVar7 = *param_1;
    if (*(char *)(lVar7 + 0x2b9) == '\0') {
      (**(code **)(*param_2 + 0x10))(param_2,param_1);
      lVar7 = *param_1;
    }
    _ZN8firebase4auth22EnableTokenAutoRefreshEPNS0_8AuthDataE(lVar7);
  }
  _ZN8firebase5Mutex7ReleaseEv(lVar3);
LAB_00bcad6c:
  if (*(long *)(lVar5 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
