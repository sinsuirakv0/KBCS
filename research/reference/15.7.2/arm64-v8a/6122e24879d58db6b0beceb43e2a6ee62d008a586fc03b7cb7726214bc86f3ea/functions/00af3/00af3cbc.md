# 00af3cbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00af3d84`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3d84.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0008.md#compare-d3e5f177b768aa65df482e0de56f8d2f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af3cbc",
  "name": "_ZN8firebase4util12JByteToUInt8EP7_JNIEnvP8_jobject",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a9927474e8d60337509c161737ac5edaf0a8ec9547d83a7e37988976a0012860",
  "source_text_sha256": "a9927474e8d60337509c161737ac5edaf0a8ec9547d83a7e37988976a0012860",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af3cbc",
        "00af3d23"
      ]
    ],
    "bytes_sha256": "7a9d6c1707cfb62693b49974c33cf93067632632018f56a6b5d3c283a5f7d4a0",
    "instruction_count": 26,
    "instruction_bytes": 104,
    "body_bytes": 104,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde280](../00bde/00bde280.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 420 bytes

~~~c

undefined4 _ZN8firebase4util12JByteToUInt8EP7_JNIEnvP8_jobject(long *param_1,undefined8 param_2)

{
  char cVar1;
  undefined4 uVar2;
  
  uVar2 = _ZN7_JNIEnv14CallByteMethodEP8_jobjectP10_jmethodIDz(param_1,param_2,DAT_010a0560);
  cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
  if (cVar1 != '\0') {
    (**(code **)(*param_1 + 0x80))(param_1);
    (**(code **)(*param_1 + 0x88))(param_1);
  }
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af3cbc"></a> `00af3cbc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00af3cc0"></a> `00af3cc0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af3cc4"></a> `00af3cc4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00af3cc8"></a> `00af3cc8` | `68 2d 00 b0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00af3ccc"></a> `00af3ccc` | `02 b1 42 f9` | ldr x2,[x8, #0x560] | `FALL_THROUGH`
<a id="insn-00af3cd0"></a> `00af3cd0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00af3cd4"></a> `00af3cd4` | `6b a9 03 94` | bl 0x00bde280 | `UNCONDITIONAL_CALL`
<a id="insn-00af3cd8"></a> `00af3cd8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af3cdc"></a> `00af3cdc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00af3ce0"></a> `00af3ce0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af3ce4"></a> `00af3ce4` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00af3ce8"></a> `00af3ce8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af3cec"></a> `00af3cec` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00af3cf0"></a> `00af3cf0` | `20 01 00 54` | b.eq 0x00af3d14 | `CONDITIONAL_JUMP`
<a id="insn-00af3cf4"></a> `00af3cf4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af3cf8"></a> `00af3cf8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af3cfc"></a> `00af3cfc` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00af3d00"></a> `00af3d00` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af3d04"></a> `00af3d04` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af3d08"></a> `00af3d08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af3d0c"></a> `00af3d0c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00af3d10"></a> `00af3d10` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af3d14"></a> `00af3d14` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af3d18"></a> `00af3d18` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00af3d1c"></a> `00af3d1c` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00af3d20"></a> `00af3d20` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af3cbc`](#insn-00af3cbc) 範囲 `[['00af3cbc', '00af3cf3']]`
  - `CONDITIONAL_JUMP` [`00af3cf0`](#insn-00af3cf0) → [`00af3d14`](#insn-00af3d14)
  - `FALL_THROUGH` [`00af3cf0`](#insn-00af3cf0) → [`00af3cf4`](#insn-00af3cf4)
- ブロック [`00af3cf4`](#insn-00af3cf4) 範囲 `[['00af3cf4', '00af3d13']]`
  - `FALL_THROUGH` [`00af3d10`](#insn-00af3d10) → [`00af3d14`](#insn-00af3d14)
- ブロック [`00af3d14`](#insn-00af3d14) 範囲 `[['00af3d14', '00af3d23']]`

## 命令位置別の参照

- [`00af3cbc`](#insn-00af3cbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3cc0`](#insn-00af3cc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3ccc`](#insn-00af3ccc) → `010a0560`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00af3cd4`](#insn-00af3cd4) → [`00bde280`](../00bde/00bde280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde280` · 推定シンボル `None` · 推定型 `None`
- [`00af3cf0`](#insn-00af3cf0) → [`00af3d14`](#insn-00af3d14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3d14`](#insn-00af3d14) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af3cbc`](#insn-00af3cbc)

~~~json
{
  "source": "00af3cbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3cc0`](#insn-00af3cc0)

~~~json
{
  "source": "00af3cc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3ccc`](#insn-00af3ccc)

~~~json
{
  "source": "00af3ccc",
  "target": "010a0560",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0560",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00af3cd4`](#insn-00af3cd4)

~~~json
{
  "source": "00af3cd4",
  "target": "00bde280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3cf0`](#insn-00af3cf0)

~~~json
{
  "source": "00af3cf0",
  "target": "00af3d14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3d14`](#insn-00af3d14)

~~~json
{
  "source": "00af3d14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
