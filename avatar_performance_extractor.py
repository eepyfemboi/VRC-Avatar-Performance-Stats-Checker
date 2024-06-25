import UnityPy
import os

from UnityPy.enums.ClassIDType import ClassIDType

def get_file_size(file_path):
    return os.path.getsize(file_path)

def get_texture_memory(env: UnityPy.Environment):
    texture_memory = 0
    for obj in env.objects:
        if obj.type.name == "Texture2D":
            #obj: ClassIDType.Texture2D = obj
            texture = obj.read()
            texture_memory += texture.m_Width * texture.m_Height * (texture.m_TextureFormat / 8)
    return texture_memory

def get_mesh_stats(env: UnityPy.Environment):
    mesh_stats = {
        'mesh_count': 0,
        'total_polygons': 0,
        'skinned_meshes': 0,
        'basic_meshes': 0,
        'bounds': []
    }
    
    for obj in env.objects:
        if obj.type.name == "Mesh":
        #if obj.type == ClassIDType.Mesh:
            mesh = obj.read()
            mesh_stats['mesh_count'] += 1
            for sub_mesh in mesh.m_SubMeshes:
                mesh_stats['total_polygons'] += sub_mesh.indexCount // 3
            #mesh_stats['bounds'].append(mesh.m_Bounds)
        
        if obj.type.name == "SkinnedMeshRenderer":
            mesh_stats['skinned_meshes'] += 1
        elif obj.type.name == "MeshRenderer":
            mesh_stats['basic_meshes'] += 1
    
    return mesh_stats

def get_dynamic_bone_stats(env: UnityPy.Environment):
    dynamic_bone_stats = {
        'components': 0,
        'collision_checks': 0,
        'colliders': 0,
        'simulated_bones': 0,
    }
    
    for obj in env.objects:
        if obj.type.name == "MonoBehaviour":
            mono_behaviour = obj.read()
            if mono_behaviour.m_Script and mono_behaviour.m_Script.name and "DynamicBone" in mono_behaviour.m_Script.name:
                dynamic_bone_stats['components'] += 1
                dynamic_bone_stats['collision_checks'] += mono_behaviour.m_Colliders.Count
                dynamic_bone_stats['colliders'] += len(mono_behaviour.m_Colliders)
                dynamic_bone_stats['simulated_bones'] += len(mono_behaviour.m_Root)
    
    return dynamic_bone_stats

def get_physbone_stats(env: UnityPy.Environment):
    physbone_stats = {
        'components': 0,
        'transforms': 0,
        'colliders': 0,
        'collision_check_count': 0,
    }
    
    for obj in env.objects:
        if obj.type.name == "MonoBehaviour":
            mono_behaviour = obj.read()
            if mono_behaviour.m_Script and mono_behaviour.m_Script.name and "PhysBone" in mono_behaviour.m_Script.name:
                physbone_stats['components'] += 1
                physbone_stats['transforms'] += len(mono_behaviour.m_Transforms)
                physbone_stats['colliders'] += len(mono_behaviour.m_Colliders)
                physbone_stats['collision_check_count'] += mono_behaviour.m_CollisionCheckCount
    
    return physbone_stats

def get_contact_count(env: UnityPy.Environment):
    contact_count = 0
    for obj in env.objects:
        if obj.type.name == "MonoBehaviour":
            mono_behaviour = obj.read()
            if mono_behaviour.m_Script and mono_behaviour.m_Script.name and "ContactReceiver" in mono_behaviour.m_Script.name:
                contact_count += 1
    
    return contact_count

def get_animator_count(env: UnityPy.Environment):
    animator_count = 0
    for obj in env.objects:
        if obj.type.name == "Animator":
            animator_count += 1
    
    return animator_count

def get_bone_count(env: UnityPy.Environment):
    bone_count = 0
    for obj in env.objects:
        if obj.type.name == "Transform":
            bone_count += 1
    
    return bone_count

def get_lights_count(env: UnityPy.Environment):
    lights_count = 0
    for obj in env.objects:
        if obj.type.name == "Light":
            lights_count += 1
    
    return lights_count

def get_particle_stats(env: UnityPy.Environment):
    particle_stats = {
        'particle_systems': 0,
        'total_max_particles': 0,
        'mesh_particle_polygons': 0,
        'particle_trails': 0,
        'particle_collisions': 0,
    }
    
    for obj in env.objects:
        if obj.type.name == "ParticleSystem":
            particle_system = obj.read()
            particle_stats['particle_systems'] += 1
            #particle_stats['total_max_particles'] += particle_system.main.maxParticles
            #if particle_system.trails.enabled:
            #    particle_stats['particle_trails'] += 1
            #if particle_system.collision.enabled:
            #    particle_stats['particle_collisions'] += 1
            
            #if particle_system.shape.shapeType == 5:  # Mesh
            #    mesh = particle_system.shape.mesh
            #    if mesh:
            #        particle_stats['mesh_particle_polygons'] += mesh.m_SubMeshes[0].indexCount // 3
    
    return particle_stats

def get_trail_renderers_count(env: UnityPy.Environment):
    trail_renderers_count = 0
    for obj in env.objects:
        if obj.type.name == "TrailRenderer":
            trail_renderers_count += 1
    
    return trail_renderers_count

def get_cloth_stats(env: UnityPy.Environment):
    cloth_stats = {
        'cloth_meshes': 0,
        'max_vertices': 0,
    }
    
    for obj in env.objects:
        if obj.type.name == "Cloth":
            cloth = obj.read()
            cloth_stats['cloth_meshes'] += 1
            cloth_stats['max_vertices'] += cloth.vertices.Count
    
    return cloth_stats

def get_collider_count(env: UnityPy.Environment):
    collider_count = 0
    for obj in env.objects:
        if obj.type.name == "Collider":
            collider_count += 1
    
    return collider_count

def get_rigidbody_count(env: UnityPy.Environment):
    rigidbody_count = 0
    for obj in env.objects:
        if obj.type.name == "Rigidbody":
            rigidbody_count += 1
    
    return rigidbody_count

def get_audio_source_count(env: UnityPy.Environment):
    audio_source_count = 0
    for obj in env.objects:
        if obj.type.name == "AudioSource":
            audio_source_count += 1
    
    return audio_source_count

def get_constraints_count(env: UnityPy.Environment):
    constraints_count = 0
    for obj in env.objects:
        if obj.type.name == "MonoBehaviour":
            mono_behaviour = obj.read()
            if mono_behaviour.m_Script and mono_behaviour.m_Script.name and "Constraint" in mono_behaviour.m_Script.name:
                constraints_count += 1
    
    return constraints_count

class MeshStats:
    def __init__(
            self,
            mesh_count: int,
            total_polygons: int,
            skinned_meshes: int,
            basic_meshes: int,
            bounds: list
        ):
        self.mesh_count = mesh_count
        self.polygons = total_polygons
        self.skinned_meshes = skinned_meshes
        self.basic_meshes = basic_meshes
        self.bounds = bounds

class DynamicBoneStats:
    def __init__(
            self,
            components: int,
            collision_checks: int,
            colliders: int,
            simulated_bones: int
        ):
        self.components = components
        self.collision_checks = collision_checks
        self.colliders = colliders
        self.simulated_bones = simulated_bones

class PhysBoneStats:
    def __init__(
            self,
            components: int,
            transforms: int,
            colliders: int,
            collision_check_count: int
        ):
        self.components = components
        self.transforms = transforms
        self.colliders = colliders
        self.collision_check_count = collision_check_count

class ParticleStats:
    def __init__(
            self,
            particle_systems: int,
            total_max_particles: int,
            mesh_particle_polygons: int,
            particle_trails: int,
            particle_collisions: int
        ):
        self.particle_systems = particle_systems
        self.total_max_particles = total_max_particles
        self.mesh_particle_polygons = mesh_particle_polygons
        self.particle_trails = particle_trails
        self.particle_collisions = particle_collisions

class ClothStats:
    def __init__(
            self,
            cloth_meshes: int,
            max_vertices: int
        ):
        self.cloth_meshes = cloth_meshes
        self.max_vertices = max_vertices

class VRCAStats:
    def __init__(
            self,
            file_size: int,
            texture_memory: int,
            mesh_stats: MeshStats,
            dynamic_bone_stats: DynamicBoneStats,
            physbone_stats: PhysBoneStats,
            contact_count: int,
            animator_count: int,
            bone_count: int,
            lights_count: int,
            particle_stats: ParticleStats,
            trail_renderers_count: int,
            cloth_stats: ClothStats,
            collider_count: int,
            rigidbody_count: int,
            audio_source_count: int,
            constraints_count: int
        ):
        self.file_size = file_size
        self.texture_memory = texture_memory
        self.mesh_stats = mesh_stats
        self.dynamic_bone_stats = dynamic_bone_stats
        self.physbone_stats = physbone_stats
        self.contacts = contact_count
        self.animators = animator_count
        self.bones = bone_count
        self.lights = lights_count
        self.particle_stats = particle_stats
        self.trail_renderers = trail_renderers_count
        self.cloth_stats = cloth_stats
        self.colliders = collider_count
        self.rigidbodies = rigidbody_count
        self.audio_sources = audio_source_count
        self.constraints = constraints_count

    @classmethod
    def from_path(cls, file_path: str):
        stats = analyze_vrca_file(file_path)
        
        file_size = stats["file_size"]
        texture_memory = stats['texture_memory']

        mesh_stats_raw = stats['mesh_stats']
        mesh_stats = MeshStats(
            mesh_count = mesh_stats_raw['mesh_count'],
            total_polygons = mesh_stats_raw['total_polygons'],
            skinned_meshes = mesh_stats_raw['skinned_meshes'],
            basic_meshes = mesh_stats_raw['basic_meshes'],
            bounds = mesh_stats_raw['bounds']
        )

        dynamic_bone_stats_raw = stats['dynamic_bone_stats']
        dynamic_bone_stats = DynamicBoneStats(
            components = dynamic_bone_stats_raw['components'],
            collision_checks = dynamic_bone_stats_raw['collision_checks'],
            colliders = dynamic_bone_stats_raw['colliders'],
            simulated_bones = dynamic_bone_stats_raw['simulated_bones']
        )
        
        physbone_stats_raw = stats['physbone_stats']
        physbone_stats = PhysBoneStats(
            components = physbone_stats_raw['components'],
            transforms = physbone_stats_raw['transforms'],
            colliders = physbone_stats_raw['colliders'],
            collision_check_count = physbone_stats_raw['collision_check_count']
        )
        
        contact_count = stats['contact_count']
        animator_count = stats['animator_count']
        bone_count = stats['bone_count']
        lights_count = stats['lights_count']
        
        particle_stats_raw = stats['particle_stats']
        particle_stats = ParticleStats(
            particle_systems = particle_stats_raw['particle_systems'],
            total_max_particles = particle_stats_raw['total_max_particles'],
            mesh_particle_polygons = particle_stats_raw['mesh_particle_polygons'],
            particle_trails = particle_stats_raw['particle_trails'],
            particle_collisions = particle_stats_raw['particle_collisions']
        )
        
        trail_renderers_count = stats['trail_renderers_count']
        
        cloth_stats_raw = stats['cloth_stats']
        cloth_stats = ClothStats(
            cloth_meshes = cloth_stats_raw['cloth_meshes'],
            max_vertices = cloth_stats_raw['max_vertices']
        )
        
        collider_count = stats['collider_count']
        rigidbody_count = stats['rigidbody_count']
        audio_source_count = stats['audio_source_count']
        constraints_count = stats['constraints_count']
        
        return cls(
            file_size = file_size,
            texture_memory = texture_memory,
            mesh_stats = mesh_stats,
            dynamic_bone_stats = dynamic_bone_stats,
            physbone_stats = physbone_stats,
            contact_count = contact_count,
            animator_count = animator_count,
            bone_count = bone_count,
            lights_count = lights_count,
            particle_stats = particle_stats,
            trail_renderers_count = trail_renderers_count,
            cloth_stats = cloth_stats,
            collider_count = collider_count,
            rigidbody_count = rigidbody_count,
            audio_source_count = audio_source_count,
            constraints_count = constraints_count
        )

def analyze_vrca_file(file_path):
    env: UnityPy.Environment = UnityPy.load(file_path)
    
    file_stats = {
        'file_size': get_file_size(file_path),
        'texture_memory': get_texture_memory(env),
        'mesh_stats': get_mesh_stats(env),
        'dynamic_bone_stats': get_dynamic_bone_stats(env),
        'physbone_stats': get_physbone_stats(env),
        'contact_count': get_contact_count(env),
        'animator_count': get_animator_count(env),
        'bone_count': get_bone_count(env),
        'lights_count': get_lights_count(env),
        'particle_stats': get_particle_stats(env),
        'trail_renderers_count': get_trail_renderers_count(env),
        'cloth_stats': get_cloth_stats(env),
        'collider_count': get_collider_count(env),
        'rigidbody_count': get_rigidbody_count(env),
        'audio_source_count': get_audio_source_count(env),
        'constraints_count': get_constraints_count(env),
    }
    
    return file_stats
