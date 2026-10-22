# 004eedec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](004eedec.md)

## 関数情報

~~~json
{
  "address": "004eedec",
  "name": "Botan::X509_CA::new_crl",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "48cae04d394c2a1634ec86e94635189928ccd25e668652a35c74631befe46f64",
  "source_text_sha256": "48cae04d394c2a1634ec86e94635189928ccd25e668652a35c74631befe46f64"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb630](../00bdb/00bdb630.md)
- [00bdce20](../00bdc/00bdce20.md)

## 疑似コード 1/1 / UTF-8 693 bytes

~~~c

/* Botan::X509_CA::new_crl(Botan::RandomNumberGenerator&, unsigned int) const */

void Botan::X509_CA::new_crl(RandomNumberGenerator *param_1,uint param_2)

{
  long lVar1;
  undefined8 uVar2;
  undefined4 in_w2;
  undefined8 local_60;
  undefined8 uStack_58;
  undefined8 local_50;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  uVar2 = std::__ndk1::chrono::system_clock::now();
  local_60 = 0;
  uStack_58 = 0;
  local_50 = 0;
  make_crl(param_1,&local_60,1,param_2,uVar2,in_w2);
  if (*(long *)(lVar1 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
