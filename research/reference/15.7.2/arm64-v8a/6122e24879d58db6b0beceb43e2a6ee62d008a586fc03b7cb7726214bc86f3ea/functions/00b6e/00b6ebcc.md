# 00b6ebcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b6ebcc.md)

## 関数情報

~~~json
{
  "address": "00b6ebcc",
  "name": "firebase::auth::User::provider_id",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d0ca37fcac1ed157ca4c7af2898ba9cc12425b7c902c8bcc9274441c9e8256ee",
  "source_text_sha256": "d0ca37fcac1ed157ca4c7af2898ba9cc12425b7c902c8bcc9274441c9e8256ee"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047495c](../00474/0047495c.md)
- [00bddfe0](../00bdd/00bddfe0.md)
- [00bde100](../00bde/00bde100.md)
- [00bde410](../00bde/00bde410.md)
- [00bde640](../00bde/00bde640.md)

## 疑似コード 1/1 / UTF-8 1241 bytes

~~~c

/* firebase::auth::User::provider_id() const */

void firebase::auth::User::provider_id(void)

{
  long in_x0;
  _JNIEnv *this;
  _JNIEnv *p_Var1;
  ulong uVar2;
  _jobject *p_Var3;
  basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *in_x8;
  undefined8 *puVar4;
  long lVar5;
  
  puVar4 = *(undefined8 **)(in_x0 + 0x98);
  if ((puVar4 == (undefined8 *)0x0) || (lVar5 = puVar4[0x40], lVar5 == 0)) {
    std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
    basic_string<decltype(nullptr)>(in_x8,"");
    return;
  }
  this = (_JNIEnv *)App::GetJNIEnv((App *)*puVar4);
  p_Var3 = DAT_010a19c0;
                    /* try { // try from 00b6ebf8 to 00c6ec0f has its CatchHandler @ 00b70724 */
  p_Var1 = (_JNIEnv *)FUN_0047495c(this,lVar5);
                    /* try { // try from 00b6ec10 to 00c6ecbb has its CatchHandler @ 00b6e3fc */
  uVar2 = util::CheckAndClearJniExceptions(this);
  if ((p_Var1 != (_JNIEnv *)0x0) && ((uVar2 & 1) == 0)) {
    util::JniStringToString((util *)this,p_Var1,p_Var3);
    return;
  }
  *(undefined8 *)in_x8 = 0;
  *(undefined8 *)(in_x8 + 8) = 0;
  *(undefined8 *)(in_x8 + 0x10) = 0;
  return;
}

~~~
