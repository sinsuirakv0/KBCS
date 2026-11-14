# 00bff5ac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bff5ac",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5ungetEv",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f050ae492ba466fddcc8d7f4dba89eb57f0594ba0087d1e88a86f1d7bd8bc102",
  "source_text_sha256": "f050ae492ba466fddcc8d7f4dba89eb57f0594ba0087d1e88a86f1d7bd8bc102"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c59340](../00c59/00c59340.md)
- [00c5ae70](../00c5a/00c5ae70.md)

## 疑似コード / UTF-8 1033 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5ungetEv(long *param_1)

{
  int iVar1;
  long *plVar2;
  long lVar3;
  uint uVar4;
  char local_24 [4];
  
  lVar3 = *(long *)(*param_1 + -0x18);
  param_1[1] = 0;
  uVar4 = *(uint *)((long)param_1 + lVar3 + 0x20) & 0xfffffffd;
  _ZNSt6__ndk18ios_base5clearEj((long)param_1 + *(long *)(*param_1 + -0x18),uVar4);
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_24,param_1,1);
  if (local_24[0] == '\0') {
    uVar4 = uVar4 | 4;
    goto LAB_00bff654;
  }
  plVar2 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
  if (plVar2 != (long *)0x0) {
    if (plVar2[2] != plVar2[3]) {
      plVar2[3] = plVar2[3] + -1;
      goto LAB_00bff654;
    }
    iVar1 = (**(code **)(*plVar2 + 0x58))(plVar2,0xffffffff);
    if (iVar1 != -1) goto LAB_00bff654;
  }
  uVar4 = uVar4 | 1;
LAB_00bff654:
  lVar3 = (long)param_1 + *(long *)(*param_1 + -0x18);
  _ZNSt6__ndk18ios_base5clearEj(lVar3,*(uint *)(lVar3 + 0x20) | uVar4);
  return param_1;
}

~~~
