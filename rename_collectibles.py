import unreal

# Define the folder path where your assets are located
FOLDER_PATH = "/Game/MainGameFolder/R_D"  # Change this to the path of your folder

# Function to rename assets in a folder
def rename_assets_in_folder(folder_path):
    # Get all assets in the folder
    asset_paths = unreal.EditorAssetLibrary.list_assets(folder_path, recursive=True, include_folder=False)

    for asset_path in asset_paths:
        # Load the asset
        asset = unreal.EditorAssetLibrary.load_asset(asset_path)
        if asset:
            # Extract the base name of the asset (without numbers and refinements)
            new_name = extract_base_name(asset_path)
            # Get the asset's directory path (for proper renaming)
            asset_dir = unreal.EditorAssetLibrary.get_path_name_for_loaded_asset(asset)
            asset_folder = "/".join(asset_dir.split("/")[:-1])  # The directory of the asset
            
            # Rename the asset
            new_asset_name = f"{new_name}_Collectible"
            new_asset_path = f"{asset_folder}/{new_asset_name}"
            
            unreal.EditorAssetLibrary.rename_asset(asset_path, new_asset_path)
            print(f"Renamed: {asset_path} -> {new_asset_path}")
        else:
            print(f"Failed to load asset: {asset_path}")

# Function to extract the base name of the asset from its path
def extract_base_name(asset_path):
    # Split the path to get the asset name with refinement details
    asset_name_with_details = asset_path.split("/")[-1].split(".")[0]
    
    # Split by underscores and take the first few words before numbers
    base_name_parts = []
    for part in asset_name_with_details.split("_"):
        if part.isdigit():
            break  # Stop when reaching the numeric portion
        base_name_parts.append(part)
    
    # Join the base name parts
    return "_".join(base_name_parts)

# Run the rename operation for all assets in the folder
rename_assets_in_folder(FOLDER_PATH)
