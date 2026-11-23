# 00af3dec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00af3d24`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3d24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-69c23c7a90207cb8f396185786f8cb3d)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00af3e30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3e30.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-fc2e599c43297d53edf6f4b788a2bd0a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af3dec",
  "name": "_ZN7_JNIEnv14CallByteMethodEP8_jobjectP10_jmethodIDz",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "22baf62e5c4a1a842a5fd9df00d8ab80f09ae2e38d412c5911a757112fa521af",
  "source_text_sha256": "22baf62e5c4a1a842a5fd9df00d8ab80f09ae2e38d412c5911a757112fa521af",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af3dec",
        "00af3e87"
      ]
    ],
    "bytes_sha256": "be10d6a3cdf75aecc13a34720c8441ef913f3f8d540d922139b851dd80bbac6b",
    "instruction_count": 39,
    "instruction_bytes": 156,
    "body_bytes": 156,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bde330](../00bde/00bde330.md)

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1006 bytes

~~~c

void _ZN7_JNIEnv14CallByteMethodEP8_jobjectP10_jmethodIDz
               (long *param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5,undefined8 param_6,undefined8 param_7,undefined8 param_8)

{
  long lVar1;
  long lVar2;
  undefined1 auStack_a0 [8];
  undefined8 local_98;
  undefined8 uStack_90;
  undefined8 local_88;
  undefined8 uStack_80;
  undefined8 local_78;
  undefined1 *local_70;
  undefined1 **ppuStack_68;
  undefined1 *puStack_60;
  undefined8 uStack_58;
  
  lVar1 = tpidr_el0;
  lVar2 = *(long *)(lVar1 + 0x28);
  puStack_60 = auStack_a0;
  ppuStack_68 = &local_70;
  uStack_58 = 0xffffff80ffffffd8;
  local_98 = param_4;
  uStack_90 = param_5;
  local_88 = param_6;
  uStack_80 = param_7;
  local_78 = param_8;
  local_70 = (undefined1 *)register0x00000008;
  (**(code **)(*param_1 + 0x148))();
  if (*(long *)(lVar1 + 0x28) == lVar2) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af3dec"></a> `00af3dec` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00af3df0"></a> `00af3df0` | `fc 4f 10 a9` | stp x28,x19,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00af3df4"></a> `00af3df4` | `fd 7b 11 a9` | stp x29,x30,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00af3df8"></a> `00af3df8` | `fd 43 04 91` | add x29,sp,#0x110 | `FALL_THROUGH`
<a id="insn-00af3dfc"></a> `00af3dfc` | `e3 93 08 a9` | stp x3,x4,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00af3e00"></a> `00af3e00` | `e5 9b 09 a9` | stp x5,x6,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00af3e04"></a> `00af3e04` | `e7 57 00 f9` | str x7,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00af3e08"></a> `00af3e08` | `e0 07 00 ad` | stp q0,q1,[sp] | `FALL_THROUGH`
<a id="insn-00af3e0c"></a> `00af3e0c` | `e2 0f 01 ad` | stp q2,q3,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af3e10"></a> `00af3e10` | `e4 17 02 ad` | stp q4,q5,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00af3e14"></a> `00af3e14` | `e6 1f 03 ad` | stp q6,q7,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00af3e18"></a> `00af3e18` | `53 d0 3b d5` | mrs x19,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00af3e1c"></a> `00af3e1c` | `6b 16 40 f9` | ldr x11,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00af3e20"></a> `00af3e20` | `e8 04 80 92` | mov x8,#-0x28 | `FALL_THROUGH`
<a id="insn-00af3e24"></a> `00af3e24` | `e9 03 00 91` | mov x9,sp | `FALL_THROUGH`
<a id="insn-00af3e28"></a> `00af3e28` | `ea 23 02 91` | add x10,sp,#0x88 | `FALL_THROUGH`
<a id="insn-00af3e2c"></a> `00af3e2c` | `08 f0 df f2` | movk x8,#0xff80, LSL #32 | `FALL_THROUGH`
<a id="insn-00af3e30"></a> `00af3e30` | `ac 43 00 91` | add x12,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00af3e34"></a> `00af3e34` | `29 01 02 91` | add x9,x9,#0x80 | `FALL_THROUGH`
<a id="insn-00af3e38"></a> `00af3e38` | `4a a1 00 91` | add x10,x10,#0x28 | `FALL_THROUGH`
<a id="insn-00af3e3c"></a> `00af3e3c` | `ab 83 1e f8` | stur x11,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00af3e40"></a> `00af3e40` | `a9 a3 3d a9` | stp x9,x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00af3e44"></a> `00af3e44` | `ac ab 3c a9` | stp x12,x10,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00af3e48"></a> `00af3e48` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00af3e4c"></a> `00af3e4c` | `a9 e3 00 d1` | sub x9,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00af3e50"></a> `00af3e50` | `21 01 40 ad` | ldp q1,q0,[x9] | `FALL_THROUGH`
<a id="insn-00af3e54"></a> `00af3e54` | `a3 83 01 d1` | sub x3,x29,#0x60 | `FALL_THROUGH`
<a id="insn-00af3e58"></a> `00af3e58` | `08 a5 40 f9` | ldr x8,[x8, #0x148] | `FALL_THROUGH`
<a id="insn-00af3e5c"></a> `00af3e5c` | `a1 03 3d ad` | stp q1,q0,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00af3e60"></a> `00af3e60` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af3e64"></a> `00af3e64` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00af3e68"></a> `00af3e68` | `a9 83 5e f8` | ldur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00af3e6c"></a> `00af3e6c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00af3e70"></a> `00af3e70` | `a1 00 00 54` | b.ne 0x00af3e84 | `CONDITIONAL_JUMP`
<a id="insn-00af3e74"></a> `00af3e74` | `fd 7b 51 a9` | ldp x29,x30,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00af3e78"></a> `00af3e78` | `fc 4f 50 a9` | ldp x28,x19,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00af3e7c"></a> `00af3e7c` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00af3e80"></a> `00af3e80` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00af3e84"></a> `00af3e84` | `6f 9c 03 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af3dec`](#insn-00af3dec) 範囲 `[['00af3dec', '00af3e73']]`
  - `CONDITIONAL_JUMP` [`00af3e70`](#insn-00af3e70) → [`00af3e84`](#insn-00af3e84)
  - `FALL_THROUGH` [`00af3e70`](#insn-00af3e70) → [`00af3e74`](#insn-00af3e74)
- ブロック [`00af3e74`](#insn-00af3e74) 範囲 `[['00af3e74', '00af3e83']]`
- ブロック [`00af3e84`](#insn-00af3e84) 範囲 `[['00af3e84', '00af3e87']]`

## 命令位置別の参照

- [`00af3df0`](#insn-00af3df0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3df4`](#insn-00af3df4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3dfc`](#insn-00af3dfc) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3e00`](#insn-00af3e00) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3e04`](#insn-00af3e04) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3e08`](#insn-00af3e08) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3e0c`](#insn-00af3e0c) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3e10`](#insn-00af3e10) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3e14`](#insn-00af3e14) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3e3c`](#insn-00af3e3c) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3e40`](#insn-00af3e40) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3e44`](#insn-00af3e44) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3e50`](#insn-00af3e50) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3e5c`](#insn-00af3e5c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3e68`](#insn-00af3e68) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3e70`](#insn-00af3e70) → [`00af3e84`](#insn-00af3e84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3e74`](#insn-00af3e74) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3e78`](#insn-00af3e78) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3e84`](#insn-00af3e84) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af3df0`](#insn-00af3df0)

~~~json
{
  "source": "00af3df0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3df4`](#insn-00af3df4)

~~~json
{
  "source": "00af3df4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3dfc`](#insn-00af3dfc)

~~~json
{
  "source": "00af3dfc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3e00`](#insn-00af3e00)

~~~json
{
  "source": "00af3e00",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3e04`](#insn-00af3e04)

~~~json
{
  "source": "00af3e04",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3e08`](#insn-00af3e08)

~~~json
{
  "source": "00af3e08",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3e0c`](#insn-00af3e0c)

~~~json
{
  "source": "00af3e0c",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3e10`](#insn-00af3e10)

~~~json
{
  "source": "00af3e10",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3e14`](#insn-00af3e14)

~~~json
{
  "source": "00af3e14",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3e3c`](#insn-00af3e3c)

~~~json
{
  "source": "00af3e3c",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3e40`](#insn-00af3e40)

~~~json
{
  "source": "00af3e40",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3e44`](#insn-00af3e44)

~~~json
{
  "source": "00af3e44",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3e50`](#insn-00af3e50)

~~~json
{
  "source": "00af3e50",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3e5c`](#insn-00af3e5c)

~~~json
{
  "source": "00af3e5c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3e68`](#insn-00af3e68)

~~~json
{
  "source": "00af3e68",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3e70`](#insn-00af3e70)

~~~json
{
  "source": "00af3e70",
  "target": "00af3e84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3e74`](#insn-00af3e74)

~~~json
{
  "source": "00af3e74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3e78`](#insn-00af3e78)

~~~json
{
  "source": "00af3e78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3e84`](#insn-00af3e84)

~~~json
{
  "source": "00af3e84",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
