# 00bcbb3c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bcba74`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcba74.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-84da9486fd89853d811696a4997aedca)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bcbb80`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbb80.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-231c8ba42800035a662f1cd5fe703ded)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbb3c",
  "name": "FUN_00bcbb3c",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f83621f0238fbaf9c8e0d010a75cbcfe1baf98b5504f75fb10f4992ba59ae1ce",
  "source_text_sha256": "f83621f0238fbaf9c8e0d010a75cbcfe1baf98b5504f75fb10f4992ba59ae1ce",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbb3c",
        "00bcbbb3"
      ]
    ],
    "bytes_sha256": "226261b80427ded5229cfbef84cbc3bf7a31831218ba41b02d1c49101c6fb0fa",
    "instruction_count": 30,
    "instruction_bytes": 120,
    "body_bytes": 120,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 529 bytes

~~~c

void FUN_00bcbb3c(long param_1,undefined8 param_2)

{
  long *plVar1;
  
  plVar1 = *(long **)(param_1 + 0x10);
  (**(code **)(*plVar1 + 0x20))(plVar1);
  if ((*(ushort *)((long)plVar1 + 9) & 0xc0) != 0x40) {
    (**(code **)(*plVar1 + 0x28))(plVar1,param_2);
  }
                    /* WARNING: Could not recover jumptable at 0x00bcbbb0. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(**(long **)(param_1 + 0x18) + 0x28))(*(long **)(param_1 + 0x18),param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbb3c"></a> `00bcbb3c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcbb40"></a> `00bcbb40` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcbb44"></a> `00bcbb44` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbb48"></a> `00bcbb48` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbb4c"></a> `00bcbb4c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcbb50"></a> `00bcbb50` | `15 08 40 f9` | ldr x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbb54"></a> `00bcbb54` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcbb58"></a> `00bcbb58` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bcbb5c"></a> `00bcbb5c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcbb60"></a> `00bcbb60` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcbb64"></a> `00bcbb64` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbb68"></a> `00bcbb68` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcbb6c"></a> `00bcbb6c` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bcbb70"></a> `00bcbb70` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcbb74"></a> `00bcbb74` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcbb78"></a> `00bcbb78` | `c0 00 00 54` | b.eq 0x00bcbb90 | `CONDITIONAL_JUMP`
<a id="insn-00bcbb7c"></a> `00bcbb7c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcbb80"></a> `00bcbb80` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcbb84"></a> `00bcbb84` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcbb88"></a> `00bcbb88` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcbb8c"></a> `00bcbb8c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcbb90"></a> `00bcbb90` | `60 0e 40 f9` | ldr x0,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bcbb94"></a> `00bcbb94` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcbb98"></a> `00bcbb98` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcbb9c"></a> `00bcbb9c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcbba0"></a> `00bcbba0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbba4"></a> `00bcbba4` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbba8"></a> `00bcbba8` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcbbac"></a> `00bcbbac` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcbbb0"></a> `00bcbbb0` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bcbb3c`](#insn-00bcbb3c) 範囲 `[['00bcbb3c', '00bcbb7b']]`
  - `CONDITIONAL_JUMP` [`00bcbb78`](#insn-00bcbb78) → [`00bcbb90`](#insn-00bcbb90)
  - `FALL_THROUGH` [`00bcbb78`](#insn-00bcbb78) → [`00bcbb7c`](#insn-00bcbb7c)
- ブロック [`00bcbb7c`](#insn-00bcbb7c) 範囲 `[['00bcbb7c', '00bcbb8f']]`
  - `FALL_THROUGH` [`00bcbb8c`](#insn-00bcbb8c) → [`00bcbb90`](#insn-00bcbb90)
- ブロック [`00bcbb90`](#insn-00bcbb90) 範囲 `[['00bcbb90', '00bcbbb3']]`

## 命令位置別の参照

- [`00bcbb40`](#insn-00bcbb40) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb44`](#insn-00bcbb44) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb48`](#insn-00bcbb48) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb78`](#insn-00bcbb78) → [`00bcbb90`](#insn-00bcbb90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbba0`](#insn-00bcbba0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbba4`](#insn-00bcbba4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbba8`](#insn-00bcbba8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbb40`](#insn-00bcbb40)

~~~json
{
  "source": "00bcbb40",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb44`](#insn-00bcbb44)

~~~json
{
  "source": "00bcbb44",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb48`](#insn-00bcbb48)

~~~json
{
  "source": "00bcbb48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb78`](#insn-00bcbb78)

~~~json
{
  "source": "00bcbb78",
  "target": "00bcbb90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbba0`](#insn-00bcbba0)

~~~json
{
  "source": "00bcbba0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbba4`](#insn-00bcbba4)

~~~json
{
  "source": "00bcbba4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbba8`](#insn-00bcbba8)

~~~json
{
  "source": "00bcbba8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
