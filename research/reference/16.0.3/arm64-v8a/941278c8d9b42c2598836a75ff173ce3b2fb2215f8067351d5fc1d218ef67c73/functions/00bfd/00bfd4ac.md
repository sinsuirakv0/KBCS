# 00bfd4ac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfd4ac",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPNS_15basic_streambufIcS2_EE",
  "size": 344,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8df2e4271da5cabb8710bde50fbc3f7034058318604713a0921f437f9d64040d",
  "source_text_sha256": "8df2e4271da5cabb8710bde50fbc3f7034058318604713a0921f437f9d64040d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c59340](../00c59/00c59340.md)
- [00c5ae70](../00c5a/00c5ae70.md)

## 疑似コード / UTF-8 1697 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPNS_15basic_streambufIcS2_EE
                 (long *param_1,long *param_2)

{
  long lVar1;
  undefined1 *puVar2;
  uint uVar3;
  int iVar4;
  long *plVar5;
  uint uVar6;
  char local_34 [4];
  
  param_1[1] = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_34,param_1,1);
  if (local_34[0] == '\0') {
    return param_1;
  }
  if (param_2 != (long *)0x0) {
LAB_00bfd518:
    plVar5 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
    if ((byte *)plVar5[3] == (byte *)plVar5[4]) {
      uVar3 = (**(code **)(*plVar5 + 0x48))();
      if (uVar3 == 0xffffffff) {
        uVar3 = 2;
        goto LAB_00bfd5c0;
      }
    }
    else {
      uVar3 = (uint)*(byte *)plVar5[3];
    }
    puVar2 = (undefined1 *)param_2[6];
    if (puVar2 == (undefined1 *)param_2[7]) {
      iVar4 = (**(code **)(*param_2 + 0x68))(param_2,uVar3 & 0xff);
      if (iVar4 == -1) goto LAB_00bfd5bc;
    }
    else {
      param_2[6] = (long)(puVar2 + 1);
      *puVar2 = (char)uVar3;
    }
    if (param_1[1] != 0x7fffffffffffffff) {
      param_1[1] = param_1[1] + 1;
    }
    plVar5 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
    if (plVar5[3] == plVar5[4]) {
      (**(code **)(*plVar5 + 0x50))();
    }
    else {
      plVar5[3] = plVar5[3] + 1;
    }
    goto LAB_00bfd518;
  }
  uVar6 = 4;
LAB_00bfd5d0:
  lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
  _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | uVar6);
  return param_1;
LAB_00bfd5bc:
  uVar3 = 0;
LAB_00bfd5c0:
  uVar6 = uVar3 | 4;
  if (param_1[1] != 0) {
    uVar6 = uVar3;
  }
  goto LAB_00bfd5d0;
}

~~~
