# 00bdad0c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6b80c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b80c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0005.md#compare-6cb1a7921b5d84c5d374b373e9bcd05c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdb134`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb134.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0010.md#compare-387305459f3e8f259abcafc09aec10f4)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdad0c",
  "name": "_ZN8firebase4auth17PhoneAuthProvider11GetInstanceEPNS0_4AuthE",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "54c8f5d666358d6ad197050ff8a09a74bdb1dbe905b2cfac0b7dd6d170abd929",
  "source_text_sha256": "54c8f5d666358d6ad197050ff8a09a74bdb1dbe905b2cfac0b7dd6d170abd929",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdad0c",
        "00bdadab"
      ]
    ],
    "bytes_sha256": "29437a2b451bf08a86534afb5635b8b5c90d3a5372557bfd80944a8fd0b19560",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57a90](../00c57/00c57a90.md)
- [00c5a7a0](../00c5a/00c5a7a0.md)
- [00c5ac80](../00c5a/00c5ac80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 751 bytes

~~~c

undefined8 * _ZN8firebase4auth17PhoneAuthProvider11GetInstanceEPNS0_4AuthE(long *param_1)

{
  long *plVar1;
  undefined8 uVar2;
  undefined8 *puVar3;
  long lVar4;
  undefined8 *puVar5;
  
  puVar5 = (undefined8 *)*param_1;
  if (puVar5[0x4c] == 0) {
    plVar1 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*puVar5);
    uVar2 = _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz
                      (plVar1,DAT_011267d0,DAT_011267e0,*(undefined8 *)(*param_1 + 0x1f8));
    puVar3 = (undefined8 *)_Znwm(0x10);
    *puVar3 = 0;
    puVar3[1] = 0;
    puVar5[0x4c] = puVar3;
    lVar4 = (**(code **)(*plVar1 + 0xa8))(plVar1,uVar2);
    plVar1 = (long *)puVar5[0x4c];
    plVar1[1] = lVar4;
    *plVar1 = *param_1;
  }
  return puVar5 + 0x4c;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdad0c"></a> `00bdad0c` | `f7 0f 1c f8` | str x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bdad10"></a> `00bdad10` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdad14"></a> `00bdad14` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdad18"></a> `00bdad18` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdad1c"></a> `00bdad1c` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bdad20"></a> `00bdad20` | `17 00 40 f9` | ldr x23,[x0] | `FALL_THROUGH`
<a id="insn-00bdad24"></a> `00bdad24` | `e8 32 41 f9` | ldr x8,[x23, #0x260] | `FALL_THROUGH`
<a id="insn-00bdad28"></a> `00bdad28` | `f4 82 09 91` | add x20,x23,#0x260 | `FALL_THROUGH`
<a id="insn-00bdad2c"></a> `00bdad2c` | `48 03 00 b5` | cbnz x8,0x00bdad94 | `CONDITIONAL_JUMP`
<a id="insn-00bdad30"></a> `00bdad30` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdad34"></a> `00bdad34` | `e0 02 40 f9` | ldr x0,[x23] | `FALL_THROUGH`
<a id="insn-00bdad38"></a> `00bdad38` | `d2 ff 01 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bdad3c"></a> `00bdad3c` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00bdad40"></a> `00bdad40` | `68 2a 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdad44"></a> `00bdad44` | `01 e9 43 f9` | ldr x1,[x8, #0x7d0] | `FALL_THROUGH`
<a id="insn-00bdad48"></a> `00bdad48` | `68 2a 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdad4c"></a> `00bdad4c` | `02 f1 43 f9` | ldr x2,[x8, #0x7e0] | `FALL_THROUGH`
<a id="insn-00bdad50"></a> `00bdad50` | `23 fd 40 f9` | ldr x3,[x9, #0x1f8] | `FALL_THROUGH`
<a id="insn-00bdad54"></a> `00bdad54` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdad58"></a> `00bdad58` | `92 fe 01 94` | bl 0x00c5a7a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdad5c"></a> `00bdad5c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdad60"></a> `00bdad60` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00bdad64"></a> `00bdad64` | `4b f3 01 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00bdad68"></a> `00bdad68` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bdad6c"></a> `00bdad6c` | `e0 32 01 f9` | str x0,[x23, #0x260] | `FALL_THROUGH`
<a id="insn-00bdad70"></a> `00bdad70` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bdad74"></a> `00bdad74` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdad78"></a> `00bdad78` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdad7c"></a> `00bdad7c` | `08 55 40 f9` | ldr x8,[x8, #0xa8] | `FALL_THROUGH`
<a id="insn-00bdad80"></a> `00bdad80` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdad84"></a> `00bdad84` | `e8 32 41 f9` | ldr x8,[x23, #0x260] | `FALL_THROUGH`
<a id="insn-00bdad88"></a> `00bdad88` | `00 05 00 f9` | str x0,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bdad8c"></a> `00bdad8c` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00bdad90"></a> `00bdad90` | `09 01 00 f9` | str x9,[x8] | `FALL_THROUGH`
<a id="insn-00bdad94"></a> `00bdad94` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdad98"></a> `00bdad98` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdad9c"></a> `00bdad9c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdada0"></a> `00bdada0` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdada4"></a> `00bdada4` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bdada8"></a> `00bdada8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdad0c`](#insn-00bdad0c) 範囲 `[['00bdad0c', '00bdad2f']]`
  - `CONDITIONAL_JUMP` [`00bdad2c`](#insn-00bdad2c) → [`00bdad94`](#insn-00bdad94)
  - `FALL_THROUGH` [`00bdad2c`](#insn-00bdad2c) → [`00bdad30`](#insn-00bdad30)
- ブロック [`00bdad30`](#insn-00bdad30) 範囲 `[['00bdad30', '00bdad93']]`
  - `FALL_THROUGH` [`00bdad90`](#insn-00bdad90) → [`00bdad94`](#insn-00bdad94)
- ブロック [`00bdad94`](#insn-00bdad94) 範囲 `[['00bdad94', '00bdadab']]`

## 命令位置別の参照

- [`00bdad0c`](#insn-00bdad0c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdad10`](#insn-00bdad10) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdad14`](#insn-00bdad14) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdad18`](#insn-00bdad18) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdad2c`](#insn-00bdad2c) → [`00bdad94`](#insn-00bdad94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdad38`](#insn-00bdad38) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bdad44`](#insn-00bdad44) → `011267d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdad4c`](#insn-00bdad4c) → `011267e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdad58`](#insn-00bdad58) → [`00c5a7a0`](../00c5a/00c5a7a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a7a0` · 推定シンボル `None` · 推定型 `None`
- [`00bdad64`](#insn-00bdad64) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00bdad98`](#insn-00bdad98) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdad9c`](#insn-00bdad9c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdada0`](#insn-00bdada0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdad0c`](#insn-00bdad0c)

~~~json
{
  "source": "00bdad0c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdad10`](#insn-00bdad10)

~~~json
{
  "source": "00bdad10",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdad14`](#insn-00bdad14)

~~~json
{
  "source": "00bdad14",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdad18`](#insn-00bdad18)

~~~json
{
  "source": "00bdad18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdad2c`](#insn-00bdad2c)

~~~json
{
  "source": "00bdad2c",
  "target": "00bdad94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdad38`](#insn-00bdad38)

~~~json
{
  "source": "00bdad38",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdad44`](#insn-00bdad44)

~~~json
{
  "source": "00bdad44",
  "target": "011267d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011267d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdad4c`](#insn-00bdad4c)

~~~json
{
  "source": "00bdad4c",
  "target": "011267e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011267e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdad58`](#insn-00bdad58)

~~~json
{
  "source": "00bdad58",
  "target": "00c5a7a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdad64`](#insn-00bdad64)

~~~json
{
  "source": "00bdad64",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdad98`](#insn-00bdad98)

~~~json
{
  "source": "00bdad98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdad9c`](#insn-00bdad9c)

~~~json
{
  "source": "00bdad9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdada0`](#insn-00bdada0)

~~~json
{
  "source": "00bdada0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
