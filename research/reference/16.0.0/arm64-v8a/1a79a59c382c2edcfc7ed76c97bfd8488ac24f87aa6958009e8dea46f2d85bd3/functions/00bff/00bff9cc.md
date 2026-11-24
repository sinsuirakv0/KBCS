# 00bff9cc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b82f84`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82f84.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-51c42e7357584854b396cdc72dcd3e54)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bffdf4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffdf4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-a222c3d59edb2456e72ade505c23cb4b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bff9cc",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE4swapERS3_",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d9c62fb3932e93eed1441149527fdad124489992bb30cc6927657248217a277c",
  "source_text_sha256": "d9c62fb3932e93eed1441149527fdad124489992bb30cc6927657248217a277c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bff9cc",
        "00bffa87"
      ]
    ],
    "bytes_sha256": "b2efae982379848d282cef4f674eaf30f7efea7fff26245822d242777fc94f63",
    "instruction_count": 47,
    "instruction_bytes": 188,
    "body_bytes": 188,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57e90](../00c57/00c57e90.md)
- [00c5a3d0](../00c5a/00c5a3d0.md)
- [00c5dee0](../00c5d/00c5dee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1299 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE4swapERS3_(long param_1,long param_2)

{
  undefined8 uVar1;
  undefined1 auStack_28 [8];
  
  _ZNSt6__ndk16localeC1ERKS0_(auStack_28,param_1 + 8);
  _ZNSt6__ndk16localeaSERKS0_(param_1 + 8,param_2 + 8);
  _ZNSt6__ndk16localeaSERKS0_(param_2 + 8,auStack_28);
  _ZNSt6__ndk16localeD1Ev(auStack_28);
  uVar1 = *(undefined8 *)(param_1 + 0x10);
  *(undefined8 *)(param_1 + 0x10) = *(undefined8 *)(param_2 + 0x10);
  *(undefined8 *)(param_2 + 0x10) = uVar1;
  uVar1 = *(undefined8 *)(param_1 + 0x18);
  *(undefined8 *)(param_1 + 0x18) = *(undefined8 *)(param_2 + 0x18);
  *(undefined8 *)(param_2 + 0x18) = uVar1;
  uVar1 = *(undefined8 *)(param_1 + 0x20);
  *(undefined8 *)(param_1 + 0x20) = *(undefined8 *)(param_2 + 0x20);
  *(undefined8 *)(param_2 + 0x20) = uVar1;
  uVar1 = *(undefined8 *)(param_1 + 0x28);
  *(undefined8 *)(param_1 + 0x28) = *(undefined8 *)(param_2 + 0x28);
  *(undefined8 *)(param_2 + 0x28) = uVar1;
  uVar1 = *(undefined8 *)(param_1 + 0x30);
  *(undefined8 *)(param_1 + 0x30) = *(undefined8 *)(param_2 + 0x30);
  *(undefined8 *)(param_2 + 0x30) = uVar1;
  uVar1 = *(undefined8 *)(param_1 + 0x38);
  *(undefined8 *)(param_1 + 0x38) = *(undefined8 *)(param_2 + 0x38);
  *(undefined8 *)(param_2 + 0x38) = uVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bff9cc"></a> `00bff9cc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bff9d0"></a> `00bff9d0` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bff9d4"></a> `00bff9d4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bff9d8"></a> `00bff9d8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bff9dc"></a> `00bff9dc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bff9e0"></a> `00bff9e0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bff9e4"></a> `00bff9e4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bff9e8"></a> `00bff9e8` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bff9ec"></a> `00bff9ec` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00bff9f0"></a> `00bff9f0` | `78 6a 01 94` | bl 0x00c5a3d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bff9f4"></a> `00bff9f4` | `80 22 00 91` | add x0,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00bff9f8"></a> `00bff9f8` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00bff9fc"></a> `00bff9fc` | `39 79 01 94` | bl 0x00c5dee0 | `UNCONDITIONAL_CALL`
<a id="insn-00bffa00"></a> `00bffa00` | `60 22 00 91` | add x0,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00bffa04"></a> `00bffa04` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bffa08"></a> `00bffa08` | `36 79 01 94` | bl 0x00c5dee0 | `UNCONDITIONAL_CALL`
<a id="insn-00bffa0c"></a> `00bffa0c` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bffa10"></a> `00bffa10` | `20 61 01 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bffa14"></a> `00bffa14` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bffa18"></a> `00bffa18` | `89 0a 40 f9` | ldr x9,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bffa1c"></a> `00bffa1c` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bffa20"></a> `00bffa20` | `69 0a 00 f9` | str x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bffa24"></a> `00bffa24` | `68 0e 40 f9` | ldr x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bffa28"></a> `00bffa28` | `89 0e 40 f9` | ldr x9,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bffa2c"></a> `00bffa2c` | `88 0e 00 f9` | str x8,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bffa30"></a> `00bffa30` | `69 0e 00 f9` | str x9,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bffa34"></a> `00bffa34` | `68 12 40 f9` | ldr x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bffa38"></a> `00bffa38` | `89 12 40 f9` | ldr x9,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bffa3c"></a> `00bffa3c` | `88 12 00 f9` | str x8,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bffa40"></a> `00bffa40` | `69 12 00 f9` | str x9,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bffa44"></a> `00bffa44` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bffa48"></a> `00bffa48` | `89 16 40 f9` | ldr x9,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bffa4c"></a> `00bffa4c` | `88 16 00 f9` | str x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bffa50"></a> `00bffa50` | `69 16 00 f9` | str x9,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bffa54"></a> `00bffa54` | `68 1a 40 f9` | ldr x8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00bffa58"></a> `00bffa58` | `89 1a 40 f9` | ldr x9,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bffa5c"></a> `00bffa5c` | `88 1a 00 f9` | str x8,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bffa60"></a> `00bffa60` | `69 1a 00 f9` | str x9,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00bffa64"></a> `00bffa64` | `68 1e 40 f9` | ldr x8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bffa68"></a> `00bffa68` | `89 1e 40 f9` | ldr x9,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00bffa6c"></a> `00bffa6c` | `88 1e 00 f9` | str x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00bffa70"></a> `00bffa70` | `69 1e 00 f9` | str x9,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bffa74"></a> `00bffa74` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bffa78"></a> `00bffa78` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bffa7c"></a> `00bffa7c` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bffa80"></a> `00bffa80` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bffa84"></a> `00bffa84` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bff9cc`](#insn-00bff9cc) 範囲 `[['00bff9cc', '00bffa87']]`

## 命令位置別の参照

- [`00bff9d4`](#insn-00bff9d4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff9d8`](#insn-00bff9d8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff9f0`](#insn-00bff9f0) → [`00c5a3d0`](../00c5a/00c5a3d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a3d0` · 推定シンボル `None` · 推定型 `None`
- [`00bff9fc`](#insn-00bff9fc) → [`00c5dee0`](../00c5d/00c5dee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dee0` · 推定シンボル `None` · 推定型 `None`
- [`00bffa08`](#insn-00bffa08) → [`00c5dee0`](../00c5d/00c5dee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dee0` · 推定シンボル `None` · 推定型 `None`
- [`00bffa10`](#insn-00bffa10) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bffa74`](#insn-00bffa74) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffa78`](#insn-00bffa78) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bff9d4`](#insn-00bff9d4)

~~~json
{
  "source": "00bff9d4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff9d8`](#insn-00bff9d8)

~~~json
{
  "source": "00bff9d8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff9f0`](#insn-00bff9f0)

~~~json
{
  "source": "00bff9f0",
  "target": "00c5a3d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bff9fc`](#insn-00bff9fc)

~~~json
{
  "source": "00bff9fc",
  "target": "00c5dee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffa08`](#insn-00bffa08)

~~~json
{
  "source": "00bffa08",
  "target": "00c5dee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffa10`](#insn-00bffa10)

~~~json
{
  "source": "00bffa10",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffa74`](#insn-00bffa74)

~~~json
{
  "source": "00bffa74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffa78`](#insn-00bffa78)

~~~json
{
  "source": "00bffa78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
