# 00bc5bcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bc5bcc",
  "name": "_ZN8firebase13remote_config8internal20RemoteConfigInternal7CleanupEv",
  "size": 956,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "44376e88ab8cba7102192ac1b34440aac27e06e3bc39b9569b179e334a847c30",
  "source_text_sha256": "44376e88ab8cba7102192ac1b34440aac27e06e3bc39b9569b179e334a847c30"
}
~~~

## 呼び出し元

- [00c5e8a0](../00c5e/00c5e8a0.md)

## 呼び出し先

- [00c58f80](../00c58/00c58f80.md)
- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5c000](../00c5c/00c5c000.md)
- [00c5c070](../00c5c/00c5c070.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5e9d0](../00c5e/00c5e9d0.md)

## 疑似コード / UTF-8 5681 bytes

~~~c

void _ZN8firebase13remote_config8internal20RemoteConfigInternal7CleanupEv(undefined8 *param_1)

{
  undefined *puVar1;
  int iVar2;
  long lVar3;
  undefined *puVar4;
  long *plVar5;
  undefined *local_48;
  undefined *puStack_40;
  long local_38;
  
  puVar4 = PTR__ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E_00c9ca18;
  lVar3 = tpidr_el0;
  local_38 = *(long *)(lVar3 + 0x28);
  puVar1 = PTR__ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E_00c9ca18 +
           4;
  local_48 = PTR__ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E_00c9ca18;
  puStack_40 = puVar1;
  _ZN8firebase5Mutex7AcquireEv(puVar1);
  _ZN8firebase5Mutex7AcquireEv(puVar1);
  *(int *)puVar4 = *(int *)puVar4 + 1;
  _ZN8firebase5Mutex7ReleaseEv(puVar4 + 4);
  _ZN8firebase5Mutex7AcquireEv(puVar4 + 4);
  iVar2 = *(int *)puVar4;
  if (iVar2 != 0) {
    *(int *)puVar4 = iVar2 + -1;
  }
  _ZN8firebase5Mutex7ReleaseEv(puVar4 + 4);
                    /* try { // try from 00bc5c48 to 00cc5c53 has its CatchHandler @ 00bc6508 */
  if (iVar2 == 2) {
    plVar5 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*param_1);
                    /* try { // try from 00bc5c54 to 00cc5cc7 has its CatchHandler @ 00bc4ce4 */
    if (DAT_01127718 != 0) {
      if (DAT_01127720 != '\0') {
        (**(code **)(*plVar5 + 0x6c0))(plVar5);
        DAT_01127720 = '\0';
      }
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar5);
      (**(code **)(*plVar5 + 0xb0))(plVar5,DAT_01127718);
      DAT_01127718 = 0;
    }
    if (DAT_01127538 != 0) {
      if (DAT_01127540 != '\0') {
                    /* try { // try from 00bc5cc8 to 00cc5cd3 has its CatchHandler @ 00bc6508 */
        (**(code **)(*plVar5 + 0x6c0))(plVar5);
        DAT_01127540 = '\0';
      }
                    /* try { // try from 00bc5cd4 to 00cc5d47 has its CatchHandler @ 00bc4ce4 */
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar5);
      (**(code **)(*plVar5 + 0xb0))(plVar5,DAT_01127538);
      DAT_01127538 = 0;
    }
    if (DAT_011275e0 != 0) {
      if (DAT_011275e8 != '\0') {
        (**(code **)(*plVar5 + 0x6c0))(plVar5);
        DAT_011275e8 = '\0';
      }
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar5);
      (**(code **)(*plVar5 + 0xb0))(plVar5,DAT_011275e0);
      DAT_011275e0 = 0;
    }
    if (DAT_01127628 != 0) {
                    /* try { // try from 00bc5d48 to 00cc5d53 has its CatchHandler @ 00bc6508 */
      if (DAT_01127630 != '\0') {
                    /* try { // try from 00bc5d54 to 00cc5dc7 has its CatchHandler @ 00bc4ce4 */
        (**(code **)(*plVar5 + 0x6c0))(plVar5);
        DAT_01127630 = '\0';
      }
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar5);
      (**(code **)(*plVar5 + 0xb0))(plVar5,DAT_01127628);
      DAT_01127628 = 0;
    }
    if (DAT_01127658 != 0) {
      if (DAT_01127660 != '\0') {
        (**(code **)(*plVar5 + 0x6c0))(plVar5);
        DAT_01127660 = '\0';
      }
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar5);
                    /* try { // try from 00bc5dc8 to 00cc5dd3 has its CatchHandler @ 00bc6508 */
      (**(code **)(*plVar5 + 0xb0))(plVar5,DAT_01127658);
      DAT_01127658 = 0;
    }
                    /* try { // try from 00bc5dd4 to 00cc5e7f has its CatchHandler @ 00bc4ce4 */
    if (DAT_01127680 != 0) {
      if (DAT_01127688 != '\0') {
        (**(code **)(*plVar5 + 0x6c0))(plVar5);
        DAT_01127688 = '\0';
      }
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar5);
      (**(code **)(*plVar5 + 0xb0))(plVar5,DAT_01127680);
      DAT_01127680 = 0;
    }
    if (DAT_011276b8 != 0) {
      if (DAT_011276c0 != '\0') {
        (**(code **)(*plVar5 + 0x6c0))(plVar5);
        DAT_011276c0 = '\0';
      }
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar5);
      (**(code **)(*plVar5 + 0xb0))(plVar5,DAT_011276b8);
      DAT_011276b8 = 0;
    }
    if (DAT_011276f8 != 0) {
                    /* try { // try from 00bc5e80 to 00cc5e8f has its CatchHandler @ 00bc6504 */
      if (DAT_01127700 != '\0') {
                    /* try { // try from 00bc5e90 to 00cc5f03 has its CatchHandler @ 00bc4ce4 */
        (**(code **)(*plVar5 + 0x6c0))(plVar5);
        DAT_01127700 = '\0';
      }
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar5);
      (**(code **)(*plVar5 + 0xb0))(plVar5,DAT_011276f8);
      DAT_011276f8 = 0;
    }
    if (DAT_01127738 != 0) {
      if (DAT_01127740 != '\0') {
        (**(code **)(*plVar5 + 0x6c0))(plVar5);
        DAT_01127740 = '\0';
      }
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar5);
      (**(code **)(*plVar5 + 0xb0))(plVar5,DAT_01127738);
      DAT_01127738 = 0;
    }
                    /* try { // try from 00bc5f04 to 00cc5f0f has its CatchHandler @ 00bc6504 */
    if (DAT_01127758 != 0) {
                    /* try { // try from 00bc5f10 to 00cc5f7b has its CatchHandler @ 00bc4ce4 */
      if (DAT_01127760 != '\0') {
        (**(code **)(*plVar5 + 0x6c0))(plVar5);
        DAT_01127760 = '\0';
      }
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar5);
      (**(code **)(*plVar5 + 0xb0))(plVar5,DAT_01127758);
      DAT_01127758 = 0;
    }
    _ZN8firebase4util9TerminateEP7_JNIEnv(plVar5);
  }
  _ZN8firebase8internal18ReferenceCountLockINS0_14ReferenceCountEED2Ev(&local_48);
  if (*(long *)(lVar3 + 0x28) == local_38) {
                    /* try { // try from 00bc5f7c to 00cc5f87 has its CatchHandler @ 00bc6504 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
