# 004ababc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](004ababc.md)

## 関数情報

~~~json
{
  "address": "004ababc",
  "name": "Botan::MD5::copy_state",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2c51decf051ce800262089bfe9d2acc3579c1e0d6f3b9c53ccab9681dea93954",
  "source_text_sha256": "2c51decf051ce800262089bfe9d2acc3579c1e0d6f3b9c53ccab9681dea93954"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [005132d4](../00513/005132d4.md)
- [0051d3cc](../0051d/0051d3cc.md)
- [00bdaf40](../00bda/00bdaf40.md)

## 疑似コード 1/1 / UTF-8 1029 bytes

~~~c

/* Botan::MD5::copy_state() const */

void Botan::MD5::copy_state(void)

{
  long lVar1;
  long lVar2;
  undefined *puVar3;
  long in_x0;
  long *plVar4;
  undefined8 *in_x8;
  long lVar5;
  long lVar6;
  long lVar7;
  long lVar8;
  
  plVar4 = operator_new(0x70);
  puVar3 = PTR_vtable_00c1b048;
  plVar4[2] = 0;
  plVar4[3] = 0;
  *plVar4 = (long)(puVar3 + 0x10);
  plVar4[1] = 0;
  FUN_0051d3cc();
  puVar3 = PTR_vtable_00c1b068;
  lVar6 = *(long *)(in_x0 + 0x28);
  lVar5 = *(long *)(in_x0 + 0x20);
  lVar8 = *(long *)(in_x0 + 0x38);
  lVar7 = *(long *)(in_x0 + 0x30);
  lVar1 = *(long *)(in_x0 + 0x40);
  lVar2 = *(long *)(in_x0 + 0x48);
  plVar4[9] = 0;
  plVar4[10] = 0;
  plVar4[5] = lVar6;
  plVar4[4] = lVar5;
  plVar4[7] = lVar8;
  plVar4[6] = lVar7;
  *plVar4 = (long)(puVar3 + 0x10);
  plVar4[8] = 0;
  FUN_005132d4(plVar4 + 8,lVar1,lVar2,lVar2 - lVar1 >> 2);
  plVar4[0xb] = 0;
  plVar4[0xc] = 0;
  plVar4[0xd] = 0;
  FUN_005132d4();
  *in_x8 = plVar4;
  return;
}

~~~
