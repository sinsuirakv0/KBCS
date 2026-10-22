# 00b5fdcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b5fdcc.md)

## 関数情報

~~~json
{
  "address": "00b5fdcc",
  "name": "firebase::auth::Auth::UseEmulator",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "04613d571272b1a29e1de63c4ea42a6eaa3f3cf48d56d0f49f753c2b3046818c",
  "source_text_sha256": "04613d571272b1a29e1de63c4ea42a6eaa3f3cf48d56d0f49f753c2b3046818c"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00551e14](../00551/00551e14.md)
- [00bddfe0](../00bdd/00bddfe0.md)
- [00bde100](../00bde/00bde100.md)

## 疑似コード 1/1 / UTF-8 1749 bytes

~~~c

/* firebase::auth::Auth::UseEmulator(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>,
   std::__ndk1::allocator<char> >, unsigned int) */

void __thiscall firebase::auth::Auth::UseEmulator(Auth *this,byte *param_2,undefined4 param_3)

{
  _JNIEnv *p_Var1;
  undefined8 uVar2;
  undefined8 *puVar3;
  
                    /* catch() { ... } // from try @ 00b5f94c with catch @ 00b5fdd0 */
                    /* catch() { ... } // from try @ 00b5fa90 with catch @ 00b5fddc */
                    /* catch() { ... } // from try @ 00b5fc00 with catch @ 00b5fde0 */
  puVar3 = *(undefined8 **)this;
                    /* catch() { ... } // from try @ 00b5fd50 with catch @ 00b5fde8
                       catch() { ... } // from try @ 00b5fd84 with catch @ 00b5fde8 */
  if ((*param_2 & 1) == 0) {
    param_2 = param_2 + 1;
  }
  else {
    param_2 = *(byte **)(param_2 + 0x10);
  }
  p_Var1 = (_JNIEnv *)App::GetJNIEnv((App *)*puVar3);
                    /* catch() { ... } // from try @ 00b5fcfc with catch @ 00b5fe08 */
                    /* catch() { ... } // from try @ 00b5f8c0 with catch @ 00b5fe0c */
                    /* catch() { ... } // from try @ 00b5f880 with catch @ 00b5fe10 */
  uVar2 = (**(code **)(*(long *)p_Var1 + 0x538))(p_Var1,param_2);
                    /* catch() { ... } // from try @ 00b5fd18 with catch @ 00b5fe14
                       catch() { ... } // from try @ 00b5fd6c with catch @ 00b5fe14 */
                    /* catch() { ... } // from try @ 00b5f9dc with catch @ 00b5fe1c */
  FUN_00551e14(p_Var1,puVar3[0x3f],DAT_010a1380,uVar2,param_3);
  (**(code **)(*(long *)p_Var1 + 0xb8))(p_Var1,uVar2);
  util::CheckAndClearJniExceptions(p_Var1);
  return;
}

~~~
